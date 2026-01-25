class Solution:
    def trap(self, height: List[int]) -> int:
        trappedWater = 0
        left = 0
        blocks = 0
        for i in range(1, len(height)):
            if height[i] >= height[left]:
                trappedWater += height[left]*(i-left-1) - blocks
                left = i
                blocks = 0
            else: blocks += height[i]

        blocks = 0
        rightMin = len(height)-1
        for i in range(len(height)-2, left-1,-1):
            if height[i] >= height[rightMin]:
                trappedWater += height[rightMin]*(rightMin-i-1) - blocks
                rightMin = i
                blocks = 0
            else: blocks += height[i]
            
        return trappedWater
