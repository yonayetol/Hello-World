class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        def mine(elem):
            return int(elem)
        nums.sort(key=mine,reverse=True)
        return nums[k-1]