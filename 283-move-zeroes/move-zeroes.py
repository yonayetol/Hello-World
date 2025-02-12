class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for place_holder in range(len(nums)):
            seeker = place_holder
            while seeker < len(nums) and nums[place_holder] == 0:
                if nums[seeker] != 0:
                    nums[place_holder],nums[seeker] = nums[seeker],nums[place_holder]
                seeker += 1
