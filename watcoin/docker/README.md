# Docker image for Bitcoin

## Build

**Execute in main directory!**

    docker build --tag watcoin \
                    --file watcoin/docker/Dockerfile \
                    .

## Run

    docker run [-d] \
                --name watcoin_0 \
                --env BITCOIN_PORT=8686 \
                --env BITCOIN_RPC_PORT=8787 \
                --env BITCOIN_REGTEST=1 \
                --env BITCOIN_RPC_DEPRECATED=generate \
                --env BITCOIN_DATA_DIR=/data \
                [--env BITCOIN_CONNECT=192.168.7.11:8686] \
                [--env BITCOIN_ENABLE_DNS] \
                watcoin

**Tip:** You can use Docker's images names in `BITCOIN_CONNECT` when you add `BITCOIN_ENABLE_DNS` env variable.

## Docker Compose

You can spawn some containers using prepared `docker-compose.yml`

    docker-compose --file watcoin/docker/docker-compose.yml up
