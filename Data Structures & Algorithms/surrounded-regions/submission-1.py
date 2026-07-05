class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def flood_fill(r : int, c : int, check : str, replace : str):
            if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == check:
                board[r][c] = replace
                for dr, dc in directions:
                    flood_fill(dr + r, dc + c, check, replace)

        def flood_from_borders(check, replace):
            for r in range(ROWS):
                flood_fill(r, 0, check, replace)
                flood_fill(r, COLS-1, check, replace)
            for c in range(COLS):
                flood_fill(0, c, check, replace)
                flood_fill(ROWS-1, c, check, replace)

        flood_from_borders("O", "T")
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        flood_from_borders("T", "O")