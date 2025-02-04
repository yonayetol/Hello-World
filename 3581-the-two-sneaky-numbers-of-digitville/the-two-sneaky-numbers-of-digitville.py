class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        new_nums = Counter(nums)
        return [i for i,c in new_nums.items() if c==2]
            