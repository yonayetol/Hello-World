class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        # total = 0
        # index_value = {i:0 for i in range(len(grid))} # for side view we need dictionary to get the maximum number from each index
        # for i in range(len(grid)):
        #     the_big = 0 # # for front view we add all big numbers from the sub_list
        #     for j in range(len(grid[i])):
        #         if grid[i][j] != 0:
        #             total += 1
                
        #         if grid[i][j] > the_big:
        #             the_big = grid[i][j]

        #         if index_value[j] < grid[i][j]:
        #             index_value[j] = grid[i][j]

        #     total += the_big
        # for i,big in index_value.items():
        #     total += big
        # return total
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