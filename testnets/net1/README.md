# Eksperyment net1
## Założenia
* Działamy na sieci -regtest 
	* niska trudność generacji bloków;
	* nie ma dns seedów;
	* niezmodyfikowany genesis bitcoin-regtest;
* 1 komputer, trzy węzły 
	* osobne foldery;
	* przesłonięcie wkodowanych portów poprzez config;
* brak minera
	* korzystamy z wycofywanej metody _generate_;
## Tworzenie folderów na węzły
Utworzyć foldery: Alice, Bob, Charlie.  
W każdym ma się znaleźć plik konfiguracyjny _bitcoin.conf_ o zawartości:

### Nodes
Wszystkie węzły na jednym komputerze:
* Alice
> regtest =1
> [regtest]
> port=8330
> rpcport=8331
> connect=127.0.0.1:8335
> deprecatedrpc=generate
* Bob
> regtest =1 
> [regtest]
> port=8332
> rpcport=8333
> connect=127.0.0.1:8335
> deprecatedrpc=generate
* Charlie
> regtest =1
> [regtest]
> rpcuser=rpc
> rpcpassword=rpc
> port=8335
> rpcport=8336
> deprecatedrpc=generate

## Testowanie
### Start Węzłów
W osobnych terminalach albo z opcją _-daemon_
> bitcoind -datadir=charlie
> bitcoind -datadir=alice
> bitcoind -datadir=bob
### Ile połączeń do Charlie?
bitcoin-cli --datadir=charlie getconnectioncount
### Generacja bloków
Generujemy 12 bloków (w naszym buildzie narazie maturity jest 10)
> bitcoin-cli -datadir=charlie generate 12
Dostajemy skróty 12 bloków, sprawdzamy stan konta charliego:
> bitcoin-cli -datadir=charlie getbalance
Wynik:
> 100.00000000
Jest tylko 100 (nie 600), ponieważ _block\_maturity_ jest równe 10, czyli coiny są ważne dopiero po 10 blokach od ich wykopania.
### Przesłanie środków do Boba
Bob generuje adres:
> bitcoin-cli -datadir=bob getnewaddress
> 2My9gwBiTCagjiqhL6DSKjgShxFX7Vnz9Vy
Charlie przesyła 10 btc:
> bitcoin-cli -datadir=charlie sendtoaddress 2My9gwBiTCagjiqhL6DSKjgShxFX7Vnz9Vy 10
> bdac943260d8c0e8cbec90d1726756ae14b51d8ecc6ccaf84e3e52969044d533
Stany kont:
> bitcoin-cli -datadir=charlie getbalance
> 89.99996260
> bitcoin-cli -datadir=bob getbalance
> 0.00000000
(Transakcja nie została potwierdzona)
Potwierdzenie transakcji w bloku:
> bitcoin-cli -datadir=charlie generate 1
bitcoin-cli -datadir=bob getbalance
10.00000000
### Transfer od Boba do Alice
> bitcoin-cli -datadir=alice getnewaddress "alice-main"
> 2N3JLoics4Z1fGdZvBrUZhV7HGh9wq8c81W
Transfer: 
> bitcoin-cli -datadir=bob sendtoaddress 2N3JLoics4Z1fGdZvBrUZhV7HGh9wq8c81W 1
> 9dd52fe583bc6eed57ab870aabf069cb3791d86cbea9a789720ec52ad39331c9
Balans:
> bitcoin-cli -datadir=bob getbalance
> 8.99996680
> bitcoin-cli -datadir=alice getbalance
> 0.00000000
Generacja bloku:
> bitcoin-cli -datadir=charlie generate 1
Nowy balans:
> bitcoin-cli -datadir=bob getbalance
> 8.99996680
> bitcoin-cli -datadir=alice getbalance
> 1.00000000
> bitcoin-cli -datadir=charlie getbalance
> 189.99996260

## Podłączenie minera
Konfiguracja portu _rpcport_ musi się zgadzać w konfiguracji _cpuminera_ i węzła.  
W tym wypadku podłączałem _minerd_ do węzła _Charlie_.  
Plik konfiguracyjny dla _minerd_" __cfg-net1.json__  
Uruchamianie minera:
> ./minerd -c cfg-net1.json --no-longpoll --no-getwork --no-stratum --coinbase-addr=2Msqbr7AXUrLwz6CXqNicUDsJ2MV6tdXZJP
gdzie 2Msqbr7AXUrLwz6CXqNicUDsJ2MV6tdXZJP to adres węzła Charlie.

### Wnioski:




