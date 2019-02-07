class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = j = 0
        for n in nums[1:]:
            if nums[i] == n:
                j = j+1
                continue
            i = i+1
            nums[i] = n
        return len(nums) - j
        # return i+1

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
s = Solution()

i = s.removeDuplicates(nums)
print(i, nums)
