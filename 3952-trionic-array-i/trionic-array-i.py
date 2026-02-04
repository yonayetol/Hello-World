class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        status,a = "Increasing", 2
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]: return False
            if status == "Increasing" and nums[i] < nums[i-1]: 
                if i < a: return False
                status, a = "Decreasing", i-1
            elif status == "Decreasing" and nums[i] > nums[i-1]: 
                status = "Increasing2"
            elif status == "Increasing2" and nums[i] < nums[i-1]: return False
        return status == "Increasing2"
