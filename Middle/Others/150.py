class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        nums = []
        ops = ["+", "-", "*", "/"]
        for i in tokens:
            if i not in ops:
                nums.append(int(i))
            else:
                a = nums.pop()
                b = nums.pop()
                if (i == "+"):
                    b += a
                elif (i == "-"):
                    b -= a
                elif (i == "*"):
                    b *= a
                elif (i == "/"):
                    b //= a
                nums.append(b)
        return nums[0]


l1 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]

res = Solution().evalRPN(l1)
print(res)