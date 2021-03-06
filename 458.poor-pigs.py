#
# @lc app=leetcode.cn id=458 lang=python3
#
# [458] 可怜的小猪
#
# https://leetcode-cn.com/problems/poor-pigs/description/
#
# algorithms
# Easy (48.16%)
# Total Accepted:    1.4K
# Total Submissions: 2.9K
# Testcase Example:  '1000\n15\n60'
#
# 有1000只水桶，其中有且只有一桶装的含有毒药，其余装的都是水。它们从外观看起来都一样。如果小猪喝了毒药，它会在15分钟内死去。
#
# 问题来了，如果需要你在一小时内，弄清楚哪只水桶含有毒药，你最少需要多少只猪？
#
# 回答这个问题，并为下列的进阶问题编写一个通用算法。
#
# 进阶:
#
# 假设有 n 只水桶，猪饮水中毒后会在 m 分钟内死亡，你需要多少猪（x）就能在 p 分钟内找出“有毒”水桶？n只水桶里有且仅有一只有毒的桶。
#
#
import math
class Solution:
    def poorPigs(self, buckets: 'int', minutesToDie: 'int', minutesToTest: 'int') -> 'int':
        if buckets == 1:
            return 0
        ary = minutesToTest // minutesToDie + 1

        return math.ceil(math.log(buckets, ary))

# print(Solution().poorPigs(1, 1, 1))