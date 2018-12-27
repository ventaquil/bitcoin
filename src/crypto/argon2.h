#ifndef BITCOIN_CRYPTO_ARGON2_H
#define BITCOIN_CRYPTO_ARGON2_H

#include <stdint.h>
#include <stdlib.h>

/** A hasher class for Argon2. */
class CARGON2
{
private:
    uint32_t s[8];
    unsigned char buf[64];
    uint64_t bytes;

public:
    static const size_t OUTPUT_SIZE = 32;

    CARGON2();
    CARGON2& Write(const unsigned char* data, size_t len);
    void Finalize(unsigned char hash[OUTPUT_SIZE]);
    CARGON2& Reset();
};

#endif // BITCOIN_CRYPTO_ARGON2_H
