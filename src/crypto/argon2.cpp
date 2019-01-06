#include <argon2.h>
#include <crypto/argon2.h>
#include <string.h>
#include <utility>

const unsigned char CARGON2::SALT[] = {'\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0'};

CARGON2::CARGON2() : buf(nullptr), bytes(0)
{
}

CARGON2& CARGON2::Write(const unsigned char* data, size_t len)
{
    unsigned char* tmp = (unsigned char*) malloc(sizeof(unsigned char) * (bytes + len));

    if (buf != nullptr) {
        memcpy(tmp, buf, bytes);
        free(buf);
    }

    buf = std::move(tmp);

    memcpy(buf + bytes, data, len);

    bytes += len;

    return *this;
}

void CARGON2::Finalize(unsigned char hash[OUTPUT_SIZE])
{
    argon2d_hash_raw(T_COST, M_COST, PARALLELISM, buf, bytes, SALT, SALT_SIZE, hash, OUTPUT_SIZE);
}

CARGON2& CARGON2::Reset()
{
    if (buf != nullptr) {
        free(buf);
        buf = nullptr;
    }

    bytes = 0;

    return *this;
}
