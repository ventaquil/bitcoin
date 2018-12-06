# Docker Qt Bitcoin image

## Build

**Execute in main directory!**

    docker build \
        --tag watcoin:qt \
        --file watcoin/docker/qt/Dockerfile \
        . # <--- very important dot

## Run

    docker run \
        --interactive \
        --tty \
        --env DISPLAY=$DISPLAY \
        --env uid=$(id -u) \
        --env gid=$(id -g) \
        --volume /tmp/.X11-unix:/tmp/.X11-unix \
        [--rm] \
        [--publish 8686:8686] \
        [--volume absolute/path/to/data:/data] \
        --hostname watcoin:qt \
        --name watcoin-qt \
        --env BITCOIN_PORT=8686 \
        --env BITCOIN_RPC_PORT=8787 \
        --env BITCOIN_REGTEST=1 \
        --env BITCOIN_RPC_DEPRECATED=generate \
        --env BITCOIN_DATA_DIR=/data \
        [--env BITCOIN_CONNECT=192.168.7.11:8686] \
        [--env BITCOIN_ENABLE_DNS] \
        watcoin:qt

**Tip:** You can use Docker's images names in `BITCOIN_CONNECT` when you add `BITCOIN_ENABLE_DNS` env variable.
