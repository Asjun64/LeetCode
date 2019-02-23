#
# @lc app=leetcode.cn id=506 lang=python3
#
# [506] 相对名次
#
# https://leetcode-cn.com/problems/relative-ranks/description/
#
# algorithms
# Easy (46.85%)
# Total Accepted:    2K
# Total Submissions: 4.3K
# Testcase Example:  '[5,4,3,2,1]'
#
# 给出 N 名运动员的成绩，找出他们的相对名次并授予前三名对应的奖牌。前三名运动员将会被分别授予 “金牌”，“银牌” 和“ 铜牌”（"Gold
# Medal", "Silver Medal", "Bronze Medal"）。
#
# (注：分数越高的选手，排名越靠前。)
#
# 示例 1:
#
#
# 输入: [5, 4, 3, 2, 1]
# 输出: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
# 解释: 前三名运动员的成绩为前三高的，因此将会分别被授予 “金牌”，“银牌”和“铜牌” ("Gold Medal", "Silver Medal" and
# "Bronze Medal").
# 余下的两名运动员，我们只需要通过他们的成绩计算将其相对名次即可。
#
# 提示:
#
#
# N 是一个正整数并且不会超过 10000。
# 所有运动员的成绩都不相同。
#
#
#
class Solution:
    def findRelativeRanks(self, nums: 'List[int]') -> 'List[str]':

        sortNums=sorted(nums,reverse=True)
        maps={}
        for i in range(len(sortNums)):
            maps[sortNums[i]]=i+1

        for i in range(len(nums)):
            if maps[nums[i]]==1:
                nums[i]='Gold Medal'
            elif maps[nums[i]]==2:
                nums[i]='Silver Medal'
            elif maps[nums[i]]==3:
                nums[i]='Bronze Medal'
            else:
                nums[i]=str(maps[nums[i]])
        return nums

    def myFun(nums):
        res = []
        tmp = nums.copy()
        tmp.sort(reverse = True)
        for i in nums:
            iIndex = tmp.index(i)
            if iIndex < 3:
                res.append(["Gold Medal", "Silver Medal", "Bronze Medal"][iIndex])
            else:
                res.append(str(iIndex+1))
        return res

# nums = [2, 4, 3, 5, 1]
# print(Solution().findRelativeRanks(nums))

