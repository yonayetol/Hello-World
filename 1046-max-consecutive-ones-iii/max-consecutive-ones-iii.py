class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        count_0 = 0
        answer = 0
        for right in range(len(nums)):
            if not nums[right]: count_0 += 1
            while count_0 > k:
                if not nums[left]: count_0 -= 1
                left += 1
            answer = max(answer,right-left+1)
        return answer