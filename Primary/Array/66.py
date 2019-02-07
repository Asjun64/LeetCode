class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        li = digits
        i = len(li)-1
        li[i] += 1
        while li[i]>9:
            li[i] = 0
            i -= 1
            if i==-1:
                return [1]+li
            else:
                li[i] += 1
        return li
