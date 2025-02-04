class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        for i,c in freq.items():
            if c >= ceil(len(nums)/2):
                return i