#!/usr/bin/env bash
docker build \
    --tag watcoin:bitcoind \
    --file watcoin/docker/bitcoind/Dockerfile \
    .
