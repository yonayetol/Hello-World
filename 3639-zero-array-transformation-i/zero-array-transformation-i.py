class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        diffArray = [0]*(len(nums)+1)
        for sub in queries:
            diffArray[sub[0]] += 1
            diffArray[sub[1]+1] -= 1

        if diffArray[0] < nums[0]: return False

        for i in range(1, len(diffArray)-1):
            diffArray[i] += diffArray[i-1]
            if nums[i] > diffArray[i]: return False

        return True