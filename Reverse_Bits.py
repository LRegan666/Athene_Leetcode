class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bits = 31
        while bits > 15:
            high = 1 if n & (1 << bits) else 0
            low = 1 if n & (1 << 31-bits) else 0
            if high ^ low:
                n ^= (1 << bits)
                n ^= (1 << 31-bits)
            bits -= 1
        return n

