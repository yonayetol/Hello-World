class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # first let's associate the height with names
        n = len(names)
        nam_hei = {heights[i]:names[i] for i in range(n)}
        # using insertion sort # inserting it where it deserve

        for i in range(1,n):
            lft = i
            while lft-1 >= 0 and heights[lft-1] < heights[i]:
                heights[lft-1], heights[i] = heights[i],heights[lft-1]
                lft -= 1
                i = lft
            
        return [nam_hei[height] for height in heights]