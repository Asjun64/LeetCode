#
# @lc app=leetcode.cn id=447 lang=python3
#
# [447] 回旋镖的数量
#
# https://leetcode-cn.com/problems/number-of-boomerangs/description/
#
# algorithms
# Easy (51.97%)
# Total Accepted:    2.8K
# Total Submissions: 5.3K
# Testcase Example:  '[[0,0],[1,0],[2,0]]'
#
# 给定平面上 n 对不同的点，“回旋镖” 是由点表示的元组 (i, j, k) ，其中 i 和 j 之间的距离和 i 和 k
# 之间的距离相等（需要考虑元组的顺序）。
#
# 找到所有回旋镖的数量。你可以假设 n 最大为 500，所有点的坐标在闭区间 [-10000, 10000] 中。
#
# 示例:
#
#
# 输入:
# [[0,0],[1,0],[2,0]]
#
# 输出:
# 2
#
# 解释:
# 两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]
#
#
#
import math
class Solution:
    def numberOfBoomerangs(self, points: 'List[List[int]]') -> 'int':


        lst = []
        n = len(points)
        for i in range(n):
            temp_lst = []
            for j in range(i+1):
                dist = (points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2
                temp_lst.append(dist)
            lst.append(temp_lst)
        for i in range(n-1):
            for j in range(i+1, n):
                lst[i].append(lst[j][i])

        sums = 0
        for each_list in lst:
            dct = {}
            nums = 0
            for item in each_list:
                dct[item] = dct.get(item, 0) + 1
            for item in dct:
                if dct[item]>=2:
                    nums += dct[item] * (dct[item] - 1)
            sums += nums

        return sums

    def myfun(self, points):
        result = 0

        points_count = len(points)

        edges = [[-1 for _ in range(points_count)] for _ in range(points_count)]

        for i in range(points_count):
            for j in range(points_count):
                m = points[i]
                n = points[j]
                distance = math.sqrt((m[0] - n[0])**2 + (m[1] - n[1])**2)
                edges[i][j] = distance
                edges[j][i] = distance

            d = {}
            for distance in edges[i]:
                d[distance] = d.get(distance, 0) + 1
            for value in d.values():
                result += value * (value - 1)

        return result

# points = [[0,0],[1,0],[2,0]]

# print(Solution().numberOfBoomerangs(points))
