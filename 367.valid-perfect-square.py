#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#
# https://leetcode-cn.com/problems/valid-perfect-square/description/
#
# algorithms
# Easy (39.10%)
# Total Accepted:    5.7K
# Total Submissions: 14.5K
# Testcase Example:  '16'
#
# 给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。
#
# 说明：不要使用任何内置的库函数，如  sqrt。
#
# 示例 1：
#
# 输入：16
# 输出：True
#
# 示例 2：
#
# 输入：14
# 输出：False
#
#
#
class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        guess = 1
        old = 0
        while abs(guess-old)>0.5:
            old = guess
            guess = (guess + num/guess)/2
        guess = int(guess)
        if guess * guess != num :
            return False
        else:
            return True

# cnt = 0
# for i in range(1, 1000):
#     flag, sqrt = Solution().isPerfectSquare(i)
#     if flag:
#         print(i, " -> ", sqrt, end="\t")
#         cnt += 1
#     if cnt == 5:
#         print()
#         cnt = 0

