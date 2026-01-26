class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        IncreasingStack = []
        heights.append(0) # 0 has the potential to clear things from the stack
        for i in range(len(heights)):
            while IncreasingStack and heights[i]<heights[IncreasingStack[-1]]:
                lastIndex = IncreasingStack.pop()
                if not IncreasingStack:
                    maxArea = max(maxArea, heights[lastIndex]*(i))
                else: maxArea = max(maxArea, heights[lastIndex]*(i-IncreasingStack[-1]-1))
            IncreasingStack.append(i)
        return maxArea