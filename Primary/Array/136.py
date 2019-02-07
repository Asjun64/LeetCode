class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = nums[0]
        for n in nums[1:]:
            i ^= n
        return i
