class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        answer,lft = sum(nums[:k])/k,0
        final = answer
        for i in range(k,len(nums)):
            answer += (nums[i] - nums[lft])/k
            final = max(final,answer)
            lft += 1
        return final