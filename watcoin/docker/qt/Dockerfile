FROM ubuntu:18.04
# Install extra tools
RUN apt-get update && \
    apt-get install -y curl vim wget && \
    rm -rf /var/lib/apt/lists/*
# Install BerkeleyDB library
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository -y ppa:bitcoin/bitcoin && \
    apt-get update && \
    apt-get install -y libdb5.3-dev libdb5.3++-dev && \
    rm -rf /var/lib/apt/lists/*
# Install basic dependencies
RUN apt-get update && \
    apt-get install -y build-essential libtool autotools-dev automake pkg-config bsdmainutils python3 && \
    apt-get install -y libssl-dev libevent-dev libboost-system-dev libboost-filesystem-dev libboost-chrono-dev libboost-test-dev libboost-thread-dev && \
    rm -rf /var/lib/apt/lists/*
# Install MiniUPnPc
RUN apt-get update && \
    apt-get install -y libminiupnpc-dev && \
    rm -rf /var/lib/apt/lists/*
# Install Qt
RUN apt-get update && \
    apt-get install -y libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools libprotobuf-dev protobuf-compiler && \
    rm -rf /var/lib/apt/lists/*
# Install sudo
RUN apt-get update && \
    apt-get install -y sudo && \
    rm -rf /var/lib/apt/lists/*
# Copy whole source
COPY . /app
# Change workdir
WORKDIR /app
# Configure solution
RUN ./autogen.sh && \
    ./configure \
        --disable-tests \
        --disable-bench \
        --with-incompatible-bdb
# Make solution
RUN make
# Install solution
RUN make install
# Change entrypoint
COPY ./watcoin/bin/docker-qt-entrypoint.sh /docker-qt-entrypoint.sh
ENTRYPOINT ["/docker-qt-entrypoint.sh"]
