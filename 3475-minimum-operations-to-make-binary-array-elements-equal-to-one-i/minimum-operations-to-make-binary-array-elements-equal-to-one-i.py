class Solution:
    def minOperations(self, nums: List[int]) -> int:
        same = [0]*len(nums)
        steps = 0
        for i in range(len(nums)):
            if same[i]%2==0 and nums[i] == 0 or same[i]%2==1 and nums[i] == 1:
                same[i] += 1
                if i+2 >= len(nums): return -1
                same[i+1] += 1
                same[i+2] += 1
                steps += 1
                
        return steps