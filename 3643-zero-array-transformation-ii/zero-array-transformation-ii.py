class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        if sum(nums) == 0: return 0
        diffArray = [0]*(len(nums)+1)
        ptr = running = 0

        for ind,sub in enumerate(queries):
            diffArray[sub[0]] += sub[2]
            diffArray[sub[1]+1] -= sub[2]
            if sub[0] <= ptr <= sub[1]:
                running += sub[2]

            while ptr < len(nums) and running >= nums[ptr]: 
                ptr += 1
                if ptr == len(nums): return ind+1
                running += diffArray[ptr]

        return -1