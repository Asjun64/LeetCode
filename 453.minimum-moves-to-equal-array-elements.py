#
# @lc app=leetcode.cn id=453 lang=python3
#
# [453] 最小移动次数使数组元素相等
#
# https://leetcode-cn.com/problems/minimum-moves-to-equal-array-elements/description/
#
# algorithms
# Easy (48.60%)
# Total Accepted:    2.4K
# Total Submissions: 4.9K
# Testcase Example:  '[1,2,3]'
#
# 给定一个长度为 n 的非空整数数组，找到让数组所有元素相等的最小移动次数。每次移动可以使 n - 1 个元素增加 1。
#
# 示例:
#
#
# 输入:
# [1,2,3]
#
# 输出:
# 3
#
# 解释:
# 只需要3次移动（注意每次移动会增加两个元素的值）：
#
# [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
#
#
#
class Solution:
    def minMoves(self, nums: 'List[int]') -> 'int':
        """
        n - 1 个元素加1
        可以视为所有元素加 1 ，再令一个元素减1
        """

        minN = min(nums)

        cnt = 0

        for i in nums:
            cnt += i - minN

        return cnt


    def myMinMoves(self, nums):
        """
        慢慢的方法
        """
        cnt = 0
        n = len(nums)
        nums.sort()
        while nums[0] != nums[-1]:
            firMax = nums[-1]
            i = -1
            while i + n > -1 and nums[i] == firMax:
                i -= 1
            tmp = firMax - nums[i]

            for j in range(1, tmp % (-1-i)+1):
                nums[i+j] -= 1
            for j in range(1, -i):
                nums[i+j] -= tmp // (-1-i)

            for i in range(n):
                nums[i] += tmp
            nums.sort()
            cnt += tmp

        return cnt
# print(Solution().minMoves([1, 999]))