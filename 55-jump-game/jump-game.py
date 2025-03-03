class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal, i = len(nums)-1, len(nums)-2
        while i > -1:
            if nums[i] >= goal-i:
                goal = i
            i -= 1
        if goal == 0:
            return True
        return False