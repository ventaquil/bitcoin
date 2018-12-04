#!/usr/bin/env bash

function exit_message {
    (>&2 echo "$@")
    exit 1

}

if [ -z "$BITCOIN_PORT" ]
then
    exit_message "BITCOIN_PORT not set!"
fi

if [ -z "$BITCOIN_RPC_PORT" ]
then
    exit_message "BITCOIN_RPC_PORT not set!"
fi

if [ -z "$BITCOIN_DATA_DIR" ]
then
    exit_message "BITCOIN_DATA_DIR not set!"
fi

if [ -z "$BITCOIN_CONF_FILE" ]
then
    BITCOIN_CONF_FILE="$BITCOIN_DATA_DIR/bitcoin.conf"
fi

if [ -n "$BITCOIN_RPC_USER" ] && [ -z "$BITCOIN_RPC_PASSWORD" ]
then
    exit_message "BITCOIN_RPC_PASSWORD not set for BITCOIN_RPC_USER!"
fi

mkdir -p "$BITCOIN_DATA_DIR" &>/dev/null
if [ "$?" != "0" ]
then
    exit_message "Failed to create \"$BITCOIN_DATA_DIR\"!"
fi

rm -f "$BITCOIN_CONF_FILE" &>/dev/null
if [ "$?" != "0" ]
then
    exit_message "Failed to remove \"$BITCOIN_CONF_FILE\"!"
fi

if [ "$BITCOIN_REGTEST" == "1" ]
then
    echo "regtest=1" >> "$BITCOIN_CONF_FILE"
    echo "[regtest]" >> "$BITCOIN_CONF_FILE"
    echo "port=$BITCOIN_PORT" >> "$BITCOIN_CONF_FILE"
    echo "rpcport=$BITCOIN_RPC_PORT" >> "$BITCOIN_CONF_FILE"
    if [ -n "$BITCOIN_RPC_USER" ] && [ -n "$BITCOIN_RPC_PASSWORD" ]
    then
        echo "rpcuser=$BITCOIN_RPC_USER" >> "$BITCOIN_CONF_FILE"
        echo "rpcpassword=$BITCOIN_RPC_PASSWORD" >> "$BITCOIN_CONF_FILE"
    fi
    if [ "$BITCOIN_SERVER" == "1" ]
    then
        echo "server=1" >> "$BITCOIN_CONF_FILE"
    fi
    if [ -n "$BITCOIN_RPC_DEPRECATED" ]
    then
        echo "deprecatedrpc=$BITCOIN_RPC_DEPRECATED" >> "$BITCOIN_CONF_FILE"
    fi
    if [ -n "$BITCOIN_CONNECT" ]
    then
        echo "connect=$BITCOIN_CONNECT" >> "$BITCOIN_CONF_FILE"
    fi
fi

bitcoind -datadir="$BITCOIN_DATA_DIR" -conf="$BITCOIN_CONF_FILE"
