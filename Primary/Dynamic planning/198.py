class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        elif length == 1:
            return nums[0]
        a = nums[0]
        b = max(nums[0], nums[1])
        i = 2
        while i < length:
            tmp = b
            b = nums[i]+a if nums[i]+a>b else b
            a = tmp
        return b


s = Solution()
l1 = [1, 2, 3, 1]
l2 = [2, 7, 9, 3, 1]

get1 = s.rob(l1)
get2 = s.rob(l2)

print(get1)
print(get2)
