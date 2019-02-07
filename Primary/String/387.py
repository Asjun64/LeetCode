class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = dict()
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] = len(s)
            else:
                d[s[i]] = i
        print(d)
        min = len(s)
        for n in d:
            if d[n]<min:
                min = d[n]
        if min == len(s):
            min = -1
        return min

str = "loveleetcocde"
s = Solution()
i = s.firstUniqChar(str)
print(i)
