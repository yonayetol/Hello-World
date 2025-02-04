class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = Counter(nums)
        
        nums = sorted(nums.items(), key = lambda x: x[1])
        
        return [nums[-i][0] for i in range(1,k+1)]
