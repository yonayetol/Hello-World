class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        solution = 0
        n = len(grid)
        for r in range(n):
            max_col = 0 
            for c in range(n):
                max_col = max(max_col,grid[c][r])
                if grid[r][c] != 0:
                    solution += 1

            solution += max_col + max(grid[r])
        return solution