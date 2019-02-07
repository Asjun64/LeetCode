class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 1
        b = 2
        i = 1
        while i < n:
            b = a + b
            a = b - a
            i = i + 1
        return a


s = Solution()

for i in range(1, 11):
    print(str(i).rjust(2), str(s.climbStairs(i)).rjust(2))
