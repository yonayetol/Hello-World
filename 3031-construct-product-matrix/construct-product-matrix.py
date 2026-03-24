class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        theProd = 1
        idxa=idxb=count=0
        for idx,lst in enumerate(grid):
            if count == 2: break
            for idx2,num in enumerate(lst):
                if num%12345 == 0: 
                    theProd *= 1
                    count += 1
                    if count == 2: break
                    idxa = idx
                    idxb = idx2
                else: 
                    theProd *= num
        
        if count > 0:
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    grid[i][j] = 0
            if count == 1:
                grid[idxa][idxb] = theProd%12345
            return grid
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                grid[i][j] = (theProd // grid[i][j]) % 12345
        return grid