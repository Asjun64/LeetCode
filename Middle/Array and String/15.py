class Solution:
    def binary(self, nums, val, left, right):
        """
        返回第一个不小于 val 的值的序号
        """
        if val > nums[right] :
            return -1
        while left < right:
            mid = (left+right)//2
            if nums[mid] >= val:
                right = mid
            else:
                left = mid+1
        return right

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<3:
            return []


        nums.sort()
        result = []
        nneg_start = self.binary(nums, 0, 0, len(nums)-1)
        if nneg_start+2 < len(nums) and nums[nneg_start]==nums[nneg_start+2]==0:
            result.append([0, 0, 0])

        for i in range(nneg_start):
            if i==0  or nums[i]!=nums[i-1]:
                n_i = -nums[i]
                if nums[-1] >= 2*n_i:
                    k_right = self.binary(nums, 2*n_i, nneg_start, len(nums)-1) # =
                    k_left = self.binary(nums, n_i//2, nneg_start, k_right)     # !=
                    j_right = k_left                                            # =
                    j_left = i+1                                                # =
                elif nums[-1] >= n_i:
                    k_right = len(nums)-1
                    k_left = self.binary(nums, n_i//2, nneg_start, k_right)
                    j_right = k_left
                    j_left = self.binary(nums, n_i-nums[-1], i+1, nneg_start)
                elif nums[-1] >= n_i//2:
                    k_right = len(nums)-1
                    k_left = self.binary(nums, n_i//2, nneg_start, k_right)
                    j_right = k_left
                    j_left = self.binary(nums, n_i-nums[-1], nneg_start, j_right)
                else:
                    continue
                if j_left == k_right:
                    continue
                if nums[k_left] == n_i/2 and k_left!=k_right:
                    k_left += 1
                for j in range(j_left, j_right+1):
                    if j==j_left or nums[j]!=nums[j-1]:
                        k = self.binary(nums, -(nums[i]+nums[j]), k_left, k_right)
                        if k!=-1 and nums[i]+nums[j]+nums[k]==0:
                            result.append([nums[i], nums[j], nums[k]])

        return result
