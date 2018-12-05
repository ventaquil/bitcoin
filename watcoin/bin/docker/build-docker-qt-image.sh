#!/usr/bin/env bash
docker build \
    --tag watcoin:qt \
    --file watcoin/docker/qt/Dockerfile \
    .
