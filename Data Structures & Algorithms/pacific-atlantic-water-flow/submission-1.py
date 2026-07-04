class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific_matrix = [[False] * COLS for _ in range(ROWS)]
        atlantic_matrix = [[False] * COLS for _ in range(ROWS)]
        directions = ((0,-1), (0, 1), (1, 0), (-1, 0))

        def dfs(r:int , c:int, ocean_matrix : List[List[bool]]):
            stack = [(r, c, 0)]
            while stack:
                r, c, height = stack.pop()
                if not (0 <= r < ROWS and 
                        0<= c < COLS and 
                        not ocean_matrix[r][c] 
                        and heights[r][c] >= height):
                    continue
                h = heights[r][c]
                ocean_matrix[r][c] = True
                for d1, d2 in directions:
                    stack.append((r+d1, c+d2, h))

        for r in range(ROWS):
            dfs(r, 0, pacific_matrix)
            dfs(r, COLS-1, atlantic_matrix)
        for c in range(COLS):
            dfs(0, c, pacific_matrix)
            dfs(ROWS-1, c, atlantic_matrix)

        result = []
        for r in range(ROWS):
            for c in range(COLS):
                if pacific_matrix[r][c] and atlantic_matrix[r][c]:
                    result.append((r, c))

        return result