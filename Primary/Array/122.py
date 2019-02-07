class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        i = j = sum = 0
        for j in range(1, len(prices)):
            if prices[i] > prices[j-1]:
                i = j
            elif prices[j-1] > prices[j]:
                sum += prices[j-1]-prices[i]
                i = j
        if prices[i] < prices[j]:
            sum += prices[j] - prices[i]
        return sum


nums = [7, 1, 5, 3, 6, 4]
# nums = [1, 2, 3, 4, 5]
# nums = [7, 4, 3, 2, 1]
s = Solution()

sum = s.maxProfit(nums)
print(sum)
