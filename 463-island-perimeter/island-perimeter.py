class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        def inbound(x,y): return 0 <= x < len(grid) and 0 <= y < len(grid[0])

        counter = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    for dx, dy in directions:
                        if not inbound(x+dx, y+dy) or grid[x+dx][y+dy] == 0:
                            counter += 1
        return counter