class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        store = {}
        for num in nums:
            if num in store:
                del store[num]
            else:
                store[num] = 1
        return not store