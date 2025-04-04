class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        left = 0
        while left < len(nums):
            if nums[left]-1 == left or nums[nums[left]-1] == nums[left]: left += 1
            else: nums[nums[left]-1], nums[left] = nums[left], nums[nums[left]-1]

        # now everything is in its except, duplicates will be placed in the place of missing numbers
        return [i+1 for i in range(len(nums)) if nums[i] != i+1]
