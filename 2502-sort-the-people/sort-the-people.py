class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # first let's associate the height with names
        n = len(names)
        nam_hei = {heights[i]:names[i] for i in range(n)}
        # using selection sort
        for i in range(n):
            tempo = i
            for j in range(i,n):
                if heights[tempo] < heights[j]:
                    tempo = j
            # swap
            heights[i],heights[tempo] = heights[tempo],heights[i]
        return [nam_hei[height] for height in heights]