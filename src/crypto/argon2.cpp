#include <crypto/argon2.h>

CARGON2::CARGON2() : bytes(0)
{
    /*
    sha256::Initialize(s);
    */
}

CARGON2& CARGON2::Write(const unsigned char* data, size_t len)
{
    /*
    const unsigned char* end = data + len;
    size_t bufsize = bytes % 64;
    if (bufsize && bufsize + len >= 64) {
        // Fill the buffer, and process it.
        memcpy(buf + bufsize, data, 64 - bufsize);
        bytes += 64 - bufsize;
        data += 64 - bufsize;
        Transform(s, buf, 1);
        bufsize = 0;
    }
    if (end - data >= 64) {
        size_t blocks = (end - data) / 64;
        Transform(s, data, blocks);
        data += 64 * blocks;
        bytes += 64 * blocks;
    }
    if (end > data) {
        // Fill the buffer with what remains.
        memcpy(buf + bufsize, data, end - data);
        bytes += end - data;
    }
    */
    return *this;
}

void CARGON2::Finalize(unsigned char hash[OUTPUT_SIZE])
{
    /*
    static const unsigned char pad[64] = {0x80};
    unsigned char sizedesc[8];
    WriteBE64(sizedesc, bytes << 3);
    Write(pad, 1 + ((119 - (bytes % 64)) % 64));
    Write(sizedesc, 8);
    WriteBE32(hash, s[0]);
    WriteBE32(hash + 4, s[1]);
    WriteBE32(hash + 8, s[2]);
    WriteBE32(hash + 12, s[3]);
    WriteBE32(hash + 16, s[4]);
    WriteBE32(hash + 20, s[5]);
    WriteBE32(hash + 24, s[6]);
    WriteBE32(hash + 28, s[7]);
    */
}

CARGON2& CARGON2::Reset()
{
    /*
    bytes = 0;
    sha256::Initialize(s);
    */
    return *this;
}
