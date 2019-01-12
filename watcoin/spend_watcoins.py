#!/usr/bin/python3
import sys
import os
import subprocess
from subprocess import Popen, PIPE

class Command:
    def __init__ (self, label, description, func):
        self.label = label
        self.description = description
        self.func = func

class CommandList:
    def __init__(self):
        self.lst = []
        self.labels = []
    def append(self, command):
        self.lst.append(command)
        self.labels = [ i.label for i in self.lst ]
    def __contains__(self, command_label):
        #print('command:', command_label)
        #print('accepted: ',self.labels)
        return (command_label in self.labels)
    def __getitem__(self, label):
        for i in self.lst:
            if i.label == label:
                return i
class UTXO:
    def __init__ (self, s):
        data = s.split(',')
        self.txid = data[0].split(':')[1][2:-1]
        self.vout= int(data[1].split(':')[1])
        self.address = data[2].split(':')[1][2:-1]
        self.ammount = float(data[4].split(':')[1])
        self.spendable = (data[6].split(':')[1][1:] == "true")
        
    def short(self):
        return [self.txid, self.vout, self.ammount, self.spendable]





        

        


def exit_script(args, prnt=False):
    sys.exit(0)

def show_help(args, prnt = True):
    ac = args[0]
    print("\nHelp page for spend_watcoins.py:\nThis program is python wrapper for bitcoin-cli, it is being created to automatize making raw transactions.\nRun program with arguments: mode bitcoin-cli-dir bitcoin.conf-dir")
    print ("Current modes:")
    print("\th, help - show this help page")
    print("\tr, run - interactive shell for some watcoin commands")
    print("\nbitcoin-cli-dir is a path to bitcoin-cli directory.")
    print("\nbitcoin.conf-dir is a path to bitcoin.conf directory.")
    print("\nExample use:")
    print("/spend_watcoins.py r /path/to/watcoin/src /path/to/directory/of/configuration")
    print("\">\" will be printed, start there your commands.")
    print("> your commands")
    print("\n\nCurently available commands:")
          
          
    for i in ac.lst:
        print(i.label + ":\n\t", i.description, "\n")
    
    

def list_utxo(args, prnt=False):
    PATH_BITCOIN, PATH_CONFDIR = args[1], args[2]
    #print(PATH_BITCOIN, PATH_CONFDIR)
    listing_utxo = subprocess.Popen([PATH_BITCOIN + "bitcoin-cli", "-datadir=" +  PATH_CONFDIR, "listunspent"], stdout=PIPE, stderr=PIPE)
    stdout, stderr = listing_utxo.communicate()
    transactions = stdout.decode("utf-8")
    if prnt:
        print(transactions)
    if stderr != b' ':
        print(stderr.decode("utf-8"))

def blockchaininfo(args, prnt=False):
    PATH_BITCOIN, PATH_CONFDIR = args[1], args[2]
    getting_info = subprocess.Popen([PATH_BITCOIN + "bitcoin-cli", "-datadir=" +  PATH_CONFDIR, "getblockchaininfo"], stdout=PIPE, stderr=PIPE)
    stdout, stderr = getting_info.communicate()
    info = stdout.decode("utf-8")
    if prnt:
        print(info)
    if stderr != b' ':
        print(stderr.decode("utf-8"))

def generate(args, prnt=False):
    PATH_BITCOIN, PATH_CONFDIR = args[1], args[2]
    num = args[3]
    mining = subprocess.Popen([PATH_BITCOIN + "bitcoin-cli", "-datadir=" +  PATH_CONFDIR, "generate", num], stdout=PIPE, stderr=PIPE)
    stdout, stderr = mining.communicate()
    info = stdout.decode("utf-8")
    if prnt:
        print(info)
    if stderr != b' ':
        print(stderr.decode("utf-8"))

def split_utxo(args, prnt=False):
    PATH_BITCOIN, PATH_CONFDIR = args[1], args[2]
    listing_utxo = subprocess.Popen([PATH_BITCOIN + "bitcoin-cli", "-datadir=" +  PATH_CONFDIR, "listunspent"], stdout=PIPE, stderr=PIPE)
    stdout, stderr = listing_utxo.communicate()
    transactions = stdout[7:-6].decode('utf-8').split("},\n  {")

    #print(stdout,'\n\n', stdout[7:-6], '\n\n')
    #for i in transactions:
    #    print(i,'\n')

    utxo_list = [ UTXO(i) for i in transactions ]
    if prnt:
        for i in utxo_list:
            print(i.short())

    return utxo_list

def balance(args, prnt=False):
    PATH_BITCOIN, PATH_CONFDIR = args[1], args[2]
    getting_info = subprocess.Popen([PATH_BITCOIN + "bitcoin-cli", "-datadir=" +  PATH_CONFDIR, "getbalance"], stdout=PIPE, stderr=PIPE)
    stdout, stderr = getting_info.communicate()
    info = stdout.decode("utf-8")
    if prnt:
        print(info)
    if stderr != b' ':
        print(stderr.decode("utf-8"))
    return float(info)

def crt(args, prnt=False):
    if len(args) < 5:
        print("To few arguments, see help.")
        return -1
    fee = 0.0001
    PATH_BITCOIN, PATH_CONFDIR = args[1], args[2]
    address = args[3]
    ammount = float(args[4])
    available_transactions = split_utxo(args, False)

    collected = 0.0
    included_tx = []
    bl = balance(args, False)
    if bl < fee + ammount:
        print ("Too few coins - balance", ammount, bl)
        return "Too few coins - balance"
    
    for i in available_transactions:
        if i.spendable:
            collected += i.ammount
            included_tx += [i]
            if collected >= fee + ammount:
                break
    if collected < ammount + fee:
        print ("Too few coins - collected")
        return "Too few coins - collected"
    command_arg1 = "\'[{ "
    for i in included_tx:
        command_arg1 += "\"txid\" :\"" + i.txid + "\", \"vout\" : " + str(i.vout) + ", "
    command_arg1 = command_arg1[:-2] + " }]\'"
    command_arg2 = "\'{" + "\"" + address + "\": " + str(ammount) + ",\"" + included_tx[0].address + "\": " + str(collected-ammount-fee) + "}\'"



    print (command_arg1, "\n", command_arg2)
    creating_tx = subprocess.Popen([PATH_BITCOIN + "bitcoin-cli", "-datadir=" +  PATH_CONFDIR, "createrawtransaction", command_arg1 + " " + command_arg2], stdout=PIPE, stderr=PIPE)
    stdout, stderr = creating_tx.communicate()
    info = stdout.decode("utf-8")
    if prnt:
        print(info)
    if stderr != b' ':
        print(stderr.decode("utf-8"))
    return info
        
    print (command_arg1, "\n", command_arg2)
    
    

    
    
              

    
    

def main(argv):
    accepted_commands = CommandList()
    accepted_commands.append(Command("help", "Shows this page.", show_help))
    accepted_commands.append(Command("quit", "Exits program.", exit_script))
    accepted_commands.append(Command("listutxo", "Lists unspent transaction outputs for wallet", list_utxo))
    accepted_commands.append(Command("bci", "Shows blockchaininfo.", blockchaininfo))
    accepted_commands.append(Command("generate", "Generates new n blocks\n\t\t needs number of blocks to mine", generate))
    accepted_commands.append(Command("splitutxo", "List unspent transactions in short form\n\t\tDevs: returns a list of UTXO", split_utxo))
    accepted_commands.append(Command("balance", "Show balance", balance))
    accepted_commands.append(Command("crt", "Create raw transaction\n\t\tUsage; crt address ammount ", crt))
    #print(accepted_commands.labels)
        

    if len(argv) < 1:
        print ("Bad arguments, please run: ./spend-watcoins.py help.")
        return -1
    if len(argv) < 3:
        PATH_BITCOIN = "bitcoind"
        PATH_CONFDIR = "./"
    else:
        PATH_BITCOIN = argv[1]
        PATH_CONFDIR = argv[2]

    if PATH_BITCOIN[-1] != '/':
        PATH_BITCOIN += "/"
    if PATH_CONFDIR[-1] != '/':
        PATH_CONFDIR += "/"
        
        
    if argv[0] == "help":
        show_help([accepted_commands, PATH_BITCOIN, PATH_CONFDIR], True)


    #print (argv[0])
    if argv[0] in ["r", "run"]:

        ext = False
        
        print("Watcoin spend script\n")
        

        print("Checking for needed files")
        #checking bitcoin-cli
        
        checking = subprocess.Popen(['ls', PATH_BITCOIN], stdout=PIPE, stderr=PIPE)
        stdout, stderr = checking.communicate()
        if "bitcoin-cli" in stdout.decode("utf-8"):
            print ("bitcoin-cli ok")
        else:
            print ("bitcoind-cli not found - exiting.")
            return -1
        checking = subprocess.Popen(['ls', PATH_CONFDIR], stdout=PIPE, stderr=PIPE)
        stdout, stderr = checking.communicate()
        if "bitcoin.conf" in stdout.decode("utf-8"):
            print ("bitcoin.conf ok")
        else:
            print ("bitcoind.conf not found - exiting.")
            return -1

        print("Awaiting commands.")

        while ext == False:
            print('> ', end='')
            full_command = input().split(' ')
            command = full_command[0]
            if command in accepted_commands:
                args = [accepted_commands, PATH_BITCOIN, PATH_CONFDIR] + full_command[1:]
                accepted_commands[command].func([ i for i in args], True)
                
            else:
                print('Command not recognised.')
            #print(command in accepted_commands)
                
    elif argv[0] in ["d", "dev"]:
        print("hello developer!")
        split_utxo(PATH_BITCOIN, PATH_CONFDIR)
                                    
            
        

        
        
        

    
    
    
    #os.system('ls ' + argv[0] + " | grep bitcoind")
    

if __name__ == "__main__":
    main(sys.argv[1:])
    
