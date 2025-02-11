class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        repetition = 0
        preceded = 0
        for i in nums:
            if i < target:
                preceded += 1
            elif i == target:
                repetition += 1
        return [preceded+i for i in range(repetition)]