class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        result = []
        line = [1]
        i = 1
        result.append(line)
        while i < numRows:
            line = [1] + [line[i]+line[i+1] for i in range(len(line)-1)] + [1]
            result.append(line)
            i = i + 1
        return result


s = Solution()

print(s.generate(5))
