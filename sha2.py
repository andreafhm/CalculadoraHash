import struct
import binascii
import math

rrot = lambda x, n: (x >> n) | (x << (32 - n))

from itertools import count, islice
primes = lambda n: islice((k for k in count(2) if all(k % d for d in range(2, k))), 0, n)

class _SHA2_32():

    _k = [int(math.modf(x ** (1/3))[0] * (1 << 32)) for x in primes(64)]

    def __init__(self, message):
        length = struct.pack('>Q', len(message) * 8)
        while len(message) > 64:
            self._handle(message[:64])
            message = message[64:]
        message += b'\x80'
        message += bytes((56 - len(message) % 64) % 64)
        message += length
        while len(message):
            self._handle(message[:64])
            message = message[64:]

    def _handle(self, chunk):
        w = list(struct.unpack('>' + 'I' * 16, chunk))

        for i in range(16, 64):
            s0 = rrot(w[i - 15], 7) ^ rrot(w[i - 15], 18) ^ (w[i - 15] >> 3)
            s1 = rrot(w[i - 2], 17) ^ rrot(w[i - 2], 19) ^ (w[i - 2] >> 10)
            w.append((w[i - 16] + s0 + w[i - 7] + s1) & 0xffffffff)

        a = self._h0
        b = self._h1
        c = self._h2
        d = self._h3
        e = self._h4
        f = self._h5
        g = self._h6
        h = self._h7

        for i in range(64):
            S1 = rrot(e, 6) ^ rrot(e, 11) ^ rrot(e, 25)
            ch = (e & f) ^ ((~e) & g)
            temp = h + S1 + ch + self._k[i] + w[i]
            d = (d + temp) & 0xffffffff
            S0 = rrot(a, 2) ^ rrot(a, 13) ^ rrot(a, 22)
            maj = (a & (b ^ c)) ^ (b & c)
            temp = (temp + S0 + maj) & 0xffffffff

            h, g, f, e, d, c, b, a = g, f, e, d, c, b, a, temp

        self._h0 = (self._h0 + a) & 0xffffffff
        self._h1 = (self._h1 + b) & 0xffffffff
        self._h2 = (self._h2 + c) & 0xffffffff
        self._h3 = (self._h3 + d) & 0xffffffff
        self._h4 = (self._h4 + e) & 0xffffffff
        self._h5 = (self._h5 + f) & 0xffffffff
        self._h6 = (self._h6 + g) & 0xffffffff
        self._h7 = (self._h7 + h) & 0xffffffff

    def hexdigest(self):
        return binascii.hexlify(self.digest()).decode()


class SHA2_256(_SHA2_32):

    _h0, _h1, _h2, _h3, _h4, _h5, _h6, _h7 = (
        0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
        0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19)

    def digest(self):
        return struct.pack('>IIIIIIII', self._h0, self._h1, self._h2,
                           self._h3, self._h4, self._h5, self._h6, self._h7)

