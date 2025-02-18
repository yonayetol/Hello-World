class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        my_dict,count,running  = Counter({0:1}),0,0
        for num in nums:
            running += num
            count += my_dict.get(running-goal,0) 
            my_dict[running] += 1
        return count