class Solution:
    def int2arr(self, n):
        res = []
        while n:
            res.append(n%10)
            n //= 10
        return res

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        arr = [n]
        while n != 1:
            res = self.int2arr(n)
            n = 0
            for i in res:
                n += i*i
            if n in arr:
                return False
            arr.append(n)
        return True


arr = Solution().int2arr(3890)
print(arr)



print(Solution().isHappy(19))