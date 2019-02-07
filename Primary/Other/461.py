class Solution(object):
    def hammingWeight(self, x, y):
        """
        :type n: int
        :rtype: int
        """
        n = x^y
        cnt = 0
        while n:
            cnt += n%2
            n //= 2
        return cnt



s = Solution()

print(s.hammingWeight(1, 4))
