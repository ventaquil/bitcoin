#ifndef BITCOIN_CRYPTO_ARGON2_H
#define BITCOIN_CRYPTO_ARGON2_H

#include <stdint.h>
#include <stdlib.h>

/** A hasher class for Argon2. */
class CARGON2
{
private:
    unsigned char* buf;
    uint64_t bytes;

public:
    static const uint32_t T_COST = 2;
    static const uint32_t M_COST = 1 << 10; // 1 MB
    static const uint32_t PARALLELISM = 2;
    static const uint32_t SALT_SIZE = 16;
    static const unsigned char SALT[SALT_SIZE];
    static const size_t OUTPUT_SIZE = 32;

    CARGON2();
    CARGON2& Write(const unsigned char* data, size_t len);
    void Finalize(unsigned char hash[OUTPUT_SIZE]);
    CARGON2& Reset();
};

#endif // BITCOIN_CRYPTO_ARGON2_H
