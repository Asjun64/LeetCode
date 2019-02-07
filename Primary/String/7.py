class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 非
        x = int(str(x)[::-1]) if x >0 else -int(str(-x)[::-1])
        return x if x < 2147483648 and x >-2147483648 else 0


        # sign = x < 0 and -1 or 1
        # x = abs(x)
        # ans = 0
        # while x:
        #     ans = ans * 10 + x % 10
        #     x //= 10
        # return sign * ans if ans <= 0x7fffffff else 0
