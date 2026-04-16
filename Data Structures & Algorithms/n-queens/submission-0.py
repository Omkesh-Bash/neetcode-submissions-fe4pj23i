from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        coln = set()
        posD = set() #(r + c)
        negD = set() #(r - c)
        board = [['.'] * n for i in range(n)]
        print(board)
# n = 4
# board = [['.'] * n for i in range(n)]
# print(board)

        
        def dfs(i : int): # i = row
            if i >= n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for j in range(n): # j = column
                if (j in coln) or (i + j in posD) or (i - j in negD):
                    continue # Don't return we just wanted to skip current iteration.
                board[i][j] = 'Q'
                coln.add(j)
                posD.add(i + j)
                negD.add(i - j)
                dfs(i+1)
                board[i][j] = '.'
                coln.remove(j)
                posD.remove(i + j)
                negD.remove(i - j)
        dfs(0)
        return res