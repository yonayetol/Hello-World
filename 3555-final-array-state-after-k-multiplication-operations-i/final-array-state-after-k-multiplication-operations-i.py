from heapq import heapify, heappush, heappop
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        sorted_index = []
        for i in range(len(nums)):
            heappush(sorted_index,[nums[i],i])    
        for i in range(k):
            poped = heappop(sorted_index)
            nums[poped[1]] *= multiplier
            heappush(sorted_index,[nums[poped[1]],poped[1]])
        return nums