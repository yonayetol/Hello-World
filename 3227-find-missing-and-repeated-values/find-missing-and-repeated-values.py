class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        twice, total, n = 0, 0, len(grid)
        for i in range(n):
            for j in range(n):
                total += abs(grid[i][j])
                a, b = ceil(abs(grid[i][j]) / n) - 1 , (abs(grid[i][j]) % n) - 1
                if grid[a][b] < 0: twice = abs(grid[i][j])
                grid[a][b] *= -1
                
        n *= n
        return [twice, (n * (n+1) //2) - (total - twice)]