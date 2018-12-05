#!/usr/bin/env bash
docker build \
    --tag watcoin \
    --file watcoin/docker/Dockerfile \
    .
