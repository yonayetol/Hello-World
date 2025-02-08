class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        answer = []
        for i in nums:
            i = abs(i)
            if nums[i-1] < 0:
                answer.append(i)
            nums[i-1] = -nums[i-1]
        return answer