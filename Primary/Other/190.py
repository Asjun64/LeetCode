class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        i = 0
        while i < 32:
            result <<= 1
            result |= n&1^0
            n >>= 1
            i = i + 1
        return result
