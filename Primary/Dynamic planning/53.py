class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = sum = nums[0]
        for i in nums[1:]:
            if sum < 0:
                sum = sum if sum > i else i
            elif sum + i < 1:
                sum = 0
            else:
                sum += i
            if sum > max:
                max = sum
        return max

s = Solution()
l1 = [-2,1,-3,4,-1,2,1,-5,4]
result = s.maxSubArray(l1)
print(result)
