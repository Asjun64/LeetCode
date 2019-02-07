class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 2:
            return True
        i = 0
        j = len(s)-1
        while i<len(s) and s[i].isalnum()==False:
            i = i+1
        while j>-1 and s[j].isalnum()==False:
            j = j-1

        s = s.lower()
        while i<j:
            if s[i] != s[j]:
                return False
            i = i+1
            j = j-1
            while s[i].isalnum()==False:
                i = i+1
            while s[j].isalnum()==False:
                j = j-1
        return True

s =Solution()
str = "A man, a plan, a canal: Panama"
print(len(str))
print(s.isPalindrome(str))
