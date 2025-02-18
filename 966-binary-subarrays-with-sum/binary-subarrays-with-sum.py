class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        my_dict,count,running  = Counter({0:1}),0,0
        for num in nums:
            running += num
            if running-goal in my_dict:
                count += my_dict[running-goal]
            if running not in my_dict:
                my_dict[running] = 1
            else:
                my_dict[running] += 1
        return count