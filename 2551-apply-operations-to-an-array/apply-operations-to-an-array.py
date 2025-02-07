class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        answer = [0]*len(nums)

        i = 0
        real_ptr = 0
        while i < len(nums):
            
            if i < len(nums)-1 and nums[i] == nums[i+1] != 0:
                answer[real_ptr] = nums[i]*2
                real_ptr += 1
                i += 1
            elif i == len(nums)-1 or nums[i] != nums[i+1] and nums[i] != 0:
                answer[real_ptr] = nums[i]
                real_ptr += 1
            i += 1
        return answer
            