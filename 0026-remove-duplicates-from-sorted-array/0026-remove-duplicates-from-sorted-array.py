class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        for n in range(len(nums)-1):
            
            if nums[i]==nums[i+1]:
                nums.pop(i)
                i-=1
            i+=1
        return len(nums)
