#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#
# https://leetcode-cn.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (52.92%)
# Total Accepted:    8.8K
# Total Submissions: 16.7K
# Testcase Example:  '3'
#
# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
#
#
#
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
#
# 示例:
#
# 输入: 3
# 输出: [1,3,3,1]
#
#
# 进阶：
#
# 你可以优化你的算法到 O(k) 空间复杂度吗？
#
#
class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [1]
        for i in range(1, rowIndex//2+1):
            num = 1
            num *= self.fun(rowIndex-i+1, rowIndex)
            num //= self.fun(1, i)
            result.append(num)
        for i in range((rowIndex+1)//2-1, -1, -1):
            result.append(result[i])
        return result

    def fun(self, left, right):
        result = 1
        for i in range(left, right+1):
            result *= i
        return result


# s = Solution()

# print(s.getRow(7))

