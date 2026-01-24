class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        LOfnums = sorted(nums)
        theMax = 0
        n = len(nums)
        for i in range(0,n,2):
            theMax = max(theMax , LOfnums[i]+LOfnums[n-i-1])
        return theMax