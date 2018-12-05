#!/usr/bin/env bash
$(echo "/usr/local/bin/bitcoin-cli -datadir=$BITCOIN_DATA_DIR $@")
