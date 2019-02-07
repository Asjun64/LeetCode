class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0
        while n :
            n //= 5
            total += n
        return total




def fun(n):
    res = 1
    while n:
        res *= n
        n -= 1
    return res

for i in range(10):
    print(i+120, fun(i+120))