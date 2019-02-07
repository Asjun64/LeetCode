class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = j = 0
        while i<m+j and j<n:
            if nums1[i] <= nums2[j]:
                i = i + 1
            else:
                nums1[i:] = [nums2[j]] + nums1[i: len(nums1)-1]
                j = j + 1
                i = i + 1
        nums1[i:i+n-j] = nums2[j:n]
        return

s = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]

s.merge(nums1, 3, nums2, 3)

print(nums1)
