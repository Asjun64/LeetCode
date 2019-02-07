class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            x = 1/x
            n = -n
        if n%2:
            return self.myPow(x*x,n//2)*x
        else:
            return self.myPow(x*x,n/2)


print(Solution().myPow(2, 1))
print(Solution().myPow(2, 5))
print(Solution().myPow(2, 10))