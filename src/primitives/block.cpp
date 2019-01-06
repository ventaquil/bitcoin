// Copyright (c) 2009-2010 Satoshi Nakamoto
// Copyright (c) 2009-2018 The Bitcoin Core developers
// Distributed under the MIT software license, see the accompanying
// file COPYING or http://www.opensource.org/licenses/mit-license.php.

#include <primitives/block.h>

#include <crypto/argon2.h>
#include <hash.h>
#include <tinyformat.h>
#include <utilstrencodings.h>
#include <crypto/common.h>

uint256 CBlockHeader::GetHash() const
{
    return SerializeHash(*this);
}

uint256 CBlockHeader::GetProofOfWorkHash() const
{
    uint256 hash;

    const size_t HEADER_SIZE = 80; // in bytes

    unsigned char input[HEADER_SIZE];

    memcpy(input, BEGIN(nVersion), 4);
    memcpy(input + 4, hashPrevBlock.begin(), 32);
    memcpy(input + 36, hashMerkleRoot.begin(), 32);
    memcpy(input + 68, BEGIN(nTime), 4);
    memcpy(input + 72, BEGIN(nBits), 4);
    memcpy(input + 76, BEGIN(nNonce), 4);

    CARGON2 argon2;
    argon2.Write(input, HEADER_SIZE)
          .Finalize((unsigned char*)&hash);
    argon2.Reset();

    return hash;
}

std::string CBlock::ToString() const
{
    std::stringstream s;
    s << strprintf("CBlock(hash=%s, ver=0x%08x, hashPrevBlock=%s, hashMerkleRoot=%s, nTime=%u, nBits=%08x, nNonce=%u, vtx=%u)\n",
        GetHash().ToString(),
        nVersion,
        hashPrevBlock.ToString(),
        hashMerkleRoot.ToString(),
        nTime, nBits, nNonce,
        vtx.size());
    for (const auto& tx : vtx) {
        s << "  " << tx->ToString() << "\n";
    }
    return s.str();
}
