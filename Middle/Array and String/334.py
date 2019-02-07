class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m1 = m2 = float("inf")
        for i in nums:
            if (m1 >= i) :
                m1 = i
            else:
                if (m2 >= i):
                    m2 = i
                else:
                    return True
        return False







arrs = [
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [4, 5, 1, 3, 7],
    [7, 3, 4, 2, 2],
    [2, 2, 2, 2, 2, 2, 2],
    [1, 2, 3, 4, 5, 6, 7],
    [2, 1, 5, 0, 3],
    [2, 5, 3, 4, 5],
    [1, 2, -10, -8, -7],
    [1, 2, -10, 9, -7],
]



for arr in arrs:
    s = Solution()
    print(s.increasingTriplet(arr))
