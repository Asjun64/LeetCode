class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) < len(nums2):
            return self.intersect(nums2, nums1)

        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        li = []
        i = j = 0
        flag = False
        while i < len(nums2):
            for n in range(j, len(nums1)):
                if nums1[n] == nums2[i]:
                    li.append(nums1[n])
                    j = n + 1
                    break
            i = i + 1
        return li
