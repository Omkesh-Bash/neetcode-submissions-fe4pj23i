class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLMS = len(heights), len(heights[0])
        pacific_set = set()
        atlantic_set = set()
        directions = ((0,-1), (0, 1), (1, 0), (-1, 0))

        def dfs(r:int , c:int, ocean_set : set, height : int):
            if (0 <= r < ROWS and 0<= c < COLMS and (r, c) not in ocean_set and heights[r][c] >= height):
                ocean_set.add((r, c))
                for d1, d2 in directions:
                    dfs(r+d1, c+d2, ocean_set, heights[r][c])

        for r in range(ROWS):
            # pacific_set.add((r, 0))
            # atlantic_set.add((r, COLMS-1))
            dfs(r, 0, pacific_set, 0)
            dfs(r, COLMS-1, atlantic_set, 0)
        for c in range(COLMS):
            # pacific_set.add((0, c))
            # atlantic_set.add((ROWS-1,c))
            dfs(0, c, pacific_set, 0)
            dfs(ROWS-1, c, atlantic_set, 0)

        return list(pacific_set.intersection(atlantic_set)) 