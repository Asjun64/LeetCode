class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        output = []
        i = 0
        s = ""
        while i < n:
            i = i + 1
            if i%3 == i%5 == 0:
                s = "FizzBuzz"
            elif i%3 == 0:
                s = "Fizz"
            elif i%5 == 0:
                s = "Buzz"
            else:
                s = str(i)
            output.append(s)
        return output

s = Solution()
print(s.fizzBuzz(15))
