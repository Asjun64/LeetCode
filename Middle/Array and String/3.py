class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        maxlen = 1
        i = 0
        j = 1
        while j < len(s):
            if s[j] in s[i:j]:
                i += s[i:j].index(s[j]) + 1
            j += 1
            if j-i > maxlen:
                maxlen = j-i
        return maxlen

s = Solution()

l1 = "pwwkew"
l1 = "bbbbb"
l1 = "abcabcbb"
l1 = "fdajuavnakjeannc"

print(s.lengthOfLongestSubstring(l1))
