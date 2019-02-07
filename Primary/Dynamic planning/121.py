class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sum = 0
        max = 0
        for i in range(len(prices[:-1])):
            prices[i] = prices[i+1]-prices[i]
        for i in prices[:-1]:
            if sum + i < 1:
                sum = 0
            else:
                sum += i
                if max < sum:
                    max = sum
        return max


s = Solution()
l1 = [7, 1, 5, 3, 6, 4]
l2 = [-6, 4, -2, 3, -2]
print(s.maxProfit(l1))
