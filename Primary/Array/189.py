class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if l < 2 or k < 1:
            return
        i = 0
        old_i = 0
        old = nums[i]
        for v in range(l) :
            i = (i+k)%l
            new = nums[i]
            nums[i] = old
            if i==old_i:
                i = (i + 1)%l
                old_i = i
                old = nums[i]
            else:
                old = new


nums = [1, 2, 3, 4, 5, 6]
s = Solution()

s.rotate(nums, 2)

print(nums)
