class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        reminder = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                left = j + 1
                right = len(nums)-1
                while left < right:
                    the_sum = nums[left] + nums[right] + nums[i] + nums[j]
                    if the_sum == target:
                        reminder.append([nums[left],nums[right],nums[i],nums[j]])
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left-1]:
                            left += 1   # for skipping the duplicates
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1

                    elif the_sum < target:
                        left += 1
                    else:
                        right -= 1
                        
        return reminder