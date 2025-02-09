class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        my_dict = {}
        n = len(nums)
        count = 0
        for i in range(n):
            if i - nums[i] not in my_dict:
                my_dict[i - nums[i]] = 0
            my_dict[i - nums[i]] += 1
            if my_dict[i - nums[i]] >= 2:
                count += my_dict[i - nums[i]]-1
        return (n*(n-1))//2 - count