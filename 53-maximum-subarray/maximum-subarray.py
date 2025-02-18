class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        answer = float("-inf")
        total = 0
        for num in nums:
            total += num
            answer = max(answer, total)
            total = max(total, 0)
        return answer