class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = len(nums)
        i = 0
        while i < len(nums):
            result ^= i ^ nums[i]
            i += 1
        return result
