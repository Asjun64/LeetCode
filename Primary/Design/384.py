import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.v = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.v

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        res = [n for n in self.v]
        i = 0
        while i < len(res):
            j = random.randint(i, len(res)-1)
            res[i], res[j] = res[j], res[i]
            i = i + 1
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

[1] mei
[1, 2]
    1 -> 1/2 不改变，1/2 改变
[1, 2, 3]
    1 -> 1/3 不改变，2/3 改变
                    2 -> 1/2 选中
