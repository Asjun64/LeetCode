class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) < 2:
            return
        length = len(matrix)
        old = new = 0
        for i in range(length//2):
            for j in range(length-i*2-1):
                old = matrix[i][i+j]
                matrix[i][i+j] = matrix[length-1-i-j][i]
                matrix[length-1-i-j][i] = matrix[length-1-i][length-1-i-j]
                matrix[length-1-i][length-1-i-j] = matrix[i+j][length-1-i]
                matrix[i+j][length-1-i] = old

matrix =[  [ 5, 1, 9,11],  [ 2, 4, 8,10],  [13, 3, 6, 7],  [15,14,12,16]]
s = Solution()

print(matrix)

s.rotate(matrix)

print(matrix)
