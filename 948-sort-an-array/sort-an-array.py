class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        counting = [0]*(10**5 + 1)
        for i in nums:
            counting[i+50000] += 1
        other = []
        for i in range(len(counting)):
            if counting[i] > 0:
                other.extend([i-50000]*counting[i])
        return other