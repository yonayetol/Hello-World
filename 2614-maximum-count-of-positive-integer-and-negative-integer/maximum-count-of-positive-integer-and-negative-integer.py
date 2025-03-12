class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        countPositive = 0
        countZero = 0
        for num in nums:
            if num > 0:
                countPositive += 1
            elif num == 0:
                countZero += 1
        return max(countPositive, len(nums)-countPositive-countZero)