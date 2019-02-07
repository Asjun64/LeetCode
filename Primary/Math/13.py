class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        string = ["I", "V", "X", "L", "C", "D", "M"]
        nums = [1, 5, 10, 50, 100, 500, 1000]

        vals = 0
        i = 0
        while i < len(s):
            i_index = string.index(s[i])
            val = nums[i_index]
            if i == len(s)-1:
                vals += val
                break
            if i_index < string.index(s[i+1]):
                val *= -1
            vals += val
            i += 1
        return vals


s = Solution()

l1 = ["III", "IV", "IX", "LVIII", "MCMXCIV"]

for i in l1:
    print(s.romanToInt(i))
