class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        for i in range(1,len(names)):
            ptr = i
            while i > 0 and heights[i-1] < heights[ptr]:
                i -= 1

            names.insert(i,names[ptr])
            heights.insert(i,heights[ptr])
            names.pop(ptr+1)
            heights.pop(ptr+1)
        return names