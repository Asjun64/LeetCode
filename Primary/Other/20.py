class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        d = dict()
        d[")"] = "("
        d["}"] = "{"
        d["]"] = "["
        for i in s:
            if i in "({[":
                stack.append(i)
            elif stack==[] or d[i] != stack.pop(-1):
                    return False
        return True if stack==[] else False
