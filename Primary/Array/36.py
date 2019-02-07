class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            li_row = set()
            li_col = set()
            li_area = set()
            cnt_row = cnt_col = cnt_area = 0
            for num in board[i]:
                if num != ".":
                    cnt_row += 1
                    li_row.add(num)
            if len(li_row) != cnt_row :
                return False

            for j in range(9):
                if board[j][i] != ".":
                    cnt_col += 1
                    li_col.add(board[j][i])
            if len(li_col) != cnt_col :
                return False

            m = i//3
            n = i%3
            for a in range(3):
                for b in range(3):
                    if board[m*3+a][n*3+b] != ".":
                        cnt_area += 1
                        li_area.add(board[m*3+a][n*3+b])
            if len(li_area) != cnt_area:
                return False
        return True
