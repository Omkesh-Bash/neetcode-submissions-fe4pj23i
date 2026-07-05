
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def replacer_dfs(r : int, c : int, check : str, replace : str):
            if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == check:
                board[r][c] = replace
                for dr, dc in directions:
                    replacer_dfs(dr + r, dc + c, check, replace)

        for r in range(ROWS):
            replacer_dfs(r, 0, "O", "T")
            replacer_dfs(r, COLS-1, "O", "T")
        for c in range(COLS):
            replacer_dfs(0, c, "O", "T")
            replacer_dfs(ROWS-1, c, "O", "T")

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(ROWS):
            replacer_dfs(r, 0, "T", "O")
            replacer_dfs(r, COLS-1, "T", "O")
        for c in range(COLS):
            replacer_dfs(0, c, "T", "O")
            replacer_dfs(ROWS-1, c, "T", "O")