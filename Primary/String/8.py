class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        is_head = False
        sign = 1
        num = 0
        for n in str:
            if is_head:
                if n.isdigit():
                    num = num*10 + int(n)
                else:
                    break
            else:
                if n in "-+" or n.isdigit():
                    if n == "-":
                        sign = -1
                    is_head = True
                    if n.isdigit():
                        num = int(n)
                elif n!=" ":
                    return 0

        if num<=0x7fffffff:
            return num * sign
        elif sign==-1:
            return 0x80000000 * -1
        else:
            return 0x7fffffff


str = "42.1"
s = Solution()
print(s.myAtoi(str))
