class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        final = [0]
        for i in nums:
            final.append(final[-1]+i)
        return final[1:]