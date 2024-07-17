class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for n in range(len(nums)-1):
            the_num = nums[n]
            the_sec = nums[n+1]
            if the_num == the_sec:
                nums[n]=nums[n]*2
                nums[n+1] = 0
        final=[]
        length = len(nums)
        for n in range(len(nums)-1,-1,-1):
            if nums[n] == 0:
                final.insert(length,0)
            else:
                final.insert(0,nums[n])
        return final
            
