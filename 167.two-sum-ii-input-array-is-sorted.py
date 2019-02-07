#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#
# https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/description/
#
# algorithms
# Easy (45.32%)
# Total Accepted:    14.1K
# Total Submissions: 31K
# Testcase Example:  '[2,7,11,15]\n9'
#
# 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
#
# 函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
#
# 说明:
#
#
# 返回的下标值（index1 和 index2）不是从零开始的。
# 你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
#
#
# 示例:
#
# 输入: numbers = [2, 7, 11, 15], target = 9
# 输出: [1,2]
# 解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
#
#


class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        index2 = len(numbers) - 1
        left = 0
        right = index2
        index1 = (left + right) // 2

        while True :
            left = 0
            right = index2
            while index1 < index2 and left < right:
                index1 = (left + right) // 2
                sum = numbers[index1] + numbers[index2]
                if sum > target:
                    right = index1
                elif sum < target:
                    left = index1+1
                else:
                    break
            if sum == target:
                break
            index2 -= 1
            while numbers[0] + numbers[index2] > target:
                index2 -= 1

        # index1 = 0
        # index2 = len(numbers) - 1
        # while True:
        #     while index1 < index2:
        #         sum = numbers[index1] + numbers[index2]
        #         if sum >= target:
        #             break
        #         index1 += 1
        #     if sum == target:
        #         break
        #     index2 -= 1

        return [index1+1, index2+1]


        """
        # leetcode-cn 范例
        l = len(numbers)
        if l < 2:
            return
        s = {}
        for i in range(l):
            if numbers[i] not in s:
                s[target-numbers[i]] = i
            else:
                return [s[numbers[i]]+1, i+1]
        """


# arr = [  12, 13, 23, 28, 43, 44, 59, 60, 61, 68,
#          70, 86, 88, 92,124,125,136,168,173,173,
#         180,199,212,221,227,230,277,282,306,314,
#         316,321,325,328,336,337,363,365,368,370,
#         370,371,375,384,387,394,400,404,414,422,
#         422,427,430,435,457,493,506,527,531,538,
#         541,546,568,583,585,587,650,652,677,691,
#         730,737,740,751,755,764,778,783,785,789,
#         794,803,809,815,847,858,863,863,874,887,
#         896,916,920,926,927,930,933,957,981,997]

# arr = [-1, 0]
# s = Solution()

# print(s.twoSum(arr, -1))
