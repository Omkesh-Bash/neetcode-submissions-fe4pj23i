class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        
        def dfs(index : int, row : int, column : int, set1 : set):
            if index == len(word)-1 and board[row][column] == word[index]:
                return True
            if board[row][column] != word[index]:
                return False
            else:
                set1.add((row, column))
                
                result = False

                if column - 1 > -1 and (row, column-1) not in set1: 
                    result = result or dfs(index+1, row, column -1, set1.copy())
                if column + 1 < n and (row, column+1) not in set1: 
                    result = result or dfs(index+1, row, column + 1, set1.copy())
                if row - 1 > -1 and (row-1, column) not in set1: 
                    result = result or dfs(index+1, row - 1, column, set1.copy())
                if row + 1 < m and (row+1, column) not in set1: 
                    result = result or dfs(index+1, row + 1, column, set1.copy())
            return result
        
        for i in range(m):
            for j in range(n):
                if dfs(0, i, j, set()):
                    return True

        return False