# Eksperyment net2
## Założenia
* Działamy na sieci -regtest 
	* niska trudność generacji bloków;
	* nie ma dns seedów;
	* niezmodyfikowany genesis bitcoin-regtest;
* 2 komputer, trzy węzły 
	* Alice i Charlie na jednej maszynie
	* Bob i Charlie, bez przesłonięcia configami;
* podłączamy minera, do charlie i bob
## Tworzenie folderów na węzły
Utworzyć foldery: Alice, Bob, Charlie.  
W każdym ma się znaleźć plik konfiguracyjny _bitcoin.conf_ o zawartości:

### Nodes
Wszystkie węzły na jednym komputerze:
* Alice
```
regtest=1
[regtest]
port=8330
rpcport=8331
connect=127.0.0.1:19696
deprecatedrpc=generate
```
* Bob
```
regtest=1 
[regtest]
connect=172.28.113.170:19696
rpcallowip=192.168.1.0/24
server=1
deprecatedrpc=generate
```
* Charlie
```
regtest=1
[regtest]
rpcuser=rpc
rpcpassword=rpc
rpcallowip=192.168.1.0/24
server=1
deprecatedrpc=generate
```
## Testowanie
Testujemy analogicznie jak sieć 1
### Wnioski:




