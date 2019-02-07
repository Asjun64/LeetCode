class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        d1 = dict()
        d2 = dict()
        for i in range(len(s)):
            if s[i] in d1:
                d1[s[i]] = d1[s[i]]+1
            else:
                d1[s[i]] = 1
            if t[i] in d2:
                d2[t[i]] = d2[t[i]]+1
            else:
                d2[t[i]] = 1
        for n in d1:
            if d2.get(n) == False or d2.get(n) != d1.get(n):
                return False
        return True
