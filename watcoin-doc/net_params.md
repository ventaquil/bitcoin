# Parametry sieci w naszej modyfikacji
## DNS seeds
Usunięte
## Porty
#### nDefaultPort:
* CMainParams: 8686
* CTestNetParams: 18686
* CRegTestParams: 19696
#### nRPCPorts:
* CMainParams: 8685
* CTestNetParams: 18685
* CRegTestParams: 19695

## Magic message:
* CMainParams:
>		pchMessageStart[0] = 0xe0;
>		pchMessageStart[1] = 0x96;
>		pchMessageStart[2] = 0xa2;
>		pchMessageStart[3] = 0x87;
* CTestNetParams:
>		pchMessageStart[0] = 0xd3;
>		pchMessageStart[1] = 0xe2;
>		pchMessageStart[2] = 0x94;
>		pchMessageStart[3] = 0xe5;
* CRegTestParams:
>		pchMessageStart[0] = 0xb0;
>		pchMessageStart[1] = 0xd1;
>		pchMessageStart[2] = 0x95;
>		pchMessageStart[3] = 0xdc;
## Adress prefixes:
Bez zmian
## Block reward:
Bez zmian
## Halving Interval:
100 bloków zamiast 210 000:
> consensus.nSubsidyHalvingInterval = 1000; //z 210000
## Max ammount:
100 000 zamiast 21 000 000 (związane z HalvingInterval)
> static const CAmount MAX_MONEY = 100000 * COIN
## Minimum chainwork:
> consensus.nMinimumChainWork = uint256S("0000000000000000000000000000000000000000000000000000000100010001");
## DEFAULT_MAX_TIP_AGE:
Maks odległość w czasie między blokami (ponad 10 lat, aby narazie działał oryginalny genesis)
> int64_t nMaxTipAge = DEFAULT_MAX_TIP_AGE * 5000;
## BlockTime
Bez zmian:
> consensus.nPowTargetSpacing = 10 * 60
## Difficulty adjustment interval
1 dzień:
> consensus.nPowTargetTimespan = 1 * 24 * 60 * 60;
