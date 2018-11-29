import random

def gen_magic_message_code():
    for i in range (4):
        print("\t\tpchMessageStart["+str(i)+"] = "+str(hex(random.randint(127,255)))+";")

