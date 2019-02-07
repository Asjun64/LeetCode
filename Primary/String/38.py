class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        s = self.countAndSay(n-1)
        result = ""
        i = 0
        j = 1
        while i<len(s):
            if i == len(s)-1:
                result = result + str(j) + str(s[i])
                return result
            elif s[i] != s[i+1]:
                result = result + str(j) + str(s[i])
                j = 1
                i = i + 1
            else:
                i = i + 1
                j = j + 1


s = Solution()
for i in range(10):
    print(s.countAndSay(i+1))
