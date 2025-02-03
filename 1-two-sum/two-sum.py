class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i in range(len(nums)):
            if target - nums[i] in store:
                return[i,store[target - nums[i]]]
            store[nums[i]] = i