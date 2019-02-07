class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack)<len(needle):
            return -1
        if len(needle)<1:
            return 0

        i = j = 0
        while i<=len(haystack)-len(needle):
            if haystack[i] == needle[0]:
                j = len(needle)-1
                while j>0 and haystack[i+j]==needle[j]:
                    j = j -1
                if j<1:
                    return i
            i = i+1
        return -1

s =Solution()

haystack = "aaaaa"
needle = "bba"

print(s.strStr(haystack, needle))
