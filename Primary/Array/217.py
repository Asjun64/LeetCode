class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # li = sorted(nums)
        # for i in range(len(li)-1):
        #     if li[i] == li[i+1]:
        #         return True
        # return False

        # 非
        return True if len(nums) != len(set(nums)) else False
