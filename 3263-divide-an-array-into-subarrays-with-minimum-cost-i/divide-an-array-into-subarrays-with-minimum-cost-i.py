class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        newNums = sorted(nums[1:])
        return nums[0]+newNums[0]+newNums[1]