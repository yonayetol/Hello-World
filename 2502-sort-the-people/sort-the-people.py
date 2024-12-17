class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # first let's associate the height with names
        n = len(names)
        nam_hei = {heights[i]:names[i] for i in range(n)}
        # using bubble sort
        for i in range(n):
            for j in range(0,n-i-1):
                if heights[j]<heights[j+1]:
                    heights[j],heights[j+1] = heights[j+1],heights[j]
        return [nam_hei[height] for height in heights]