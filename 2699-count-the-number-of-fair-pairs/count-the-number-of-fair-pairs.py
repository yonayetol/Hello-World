from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        count = 0
        n = len(nums)

        for left in range(n):
            upper_bound = upper - nums[left]
            lower_bound = lower - nums[left]
            
            right_high = bisect_right(nums, upper_bound, left + 1)
            right_low = bisect_left(nums, lower_bound, left + 1)
            
            count += (right_high - right_low)

        return count