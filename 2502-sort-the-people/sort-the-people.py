class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(names)):
            ptr = i
            for j in range(i+1,len(names)):
                if heights[ptr] < heights[j]:
                    ptr = j
            names[i], names[ptr] = names[ptr], names[i]
            heights[i], heights[ptr] = heights[ptr], heights[i]
        return names