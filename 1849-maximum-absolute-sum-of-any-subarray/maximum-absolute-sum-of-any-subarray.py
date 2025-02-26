class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        ans = neg_catch = pos_catch = 0
        for i in range(len(nums)):
            neg_catch = min(0 , neg_catch + nums[i])
            pos_catch = max(0 , pos_catch + nums[i])
            ans = max(abs(neg_catch), pos_catch, ans)
        return ans