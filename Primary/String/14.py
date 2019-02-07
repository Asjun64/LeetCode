class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        min_len = len(strs[0])
        min_str = ""
        for i in range(len(strs)):
            if len(strs[i]) <= min_len:
                min_len = len(strs[i])
                min_str = strs[i]

        i = 0
        while i < len(min_str):
            for n in strs:
                if min_str[i] != n[i]:
                    return min_str[0:i]
            i = i + 1

        return min_str[0:i]



s =Solution()

strs = ["flower", "flow", "flight", "fludn", "fladd", "flooo"]
strs = ["a"]
ss = s.longestCommonPrefix(strs)
print(ss)
