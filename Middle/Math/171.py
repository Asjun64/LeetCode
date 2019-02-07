class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        # cnt = 0
        # iSum = 0
        # for c in s[::-1]:
        #     iSum += 26**cnt*(ord(c)-64)
        #     cnt += 1
        # return iSum

        iSum = 0
        for c in s:
            iSum = iSum*26 + ord(c) - 64
        return iSum

print(Solution().titleToNumber("ZY"))
print(Solution().titleToNumber("Y"))