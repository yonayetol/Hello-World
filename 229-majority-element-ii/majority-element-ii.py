class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        new_nums = Counter(nums)
        return [i for i,c in new_nums.items() if c > floor(len(nums)/3)]
