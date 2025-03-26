from bisect import bisect_left, bisect_right
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = bisect_left(nums, target)
        sec = bisect_right(nums, target)
        if first == sec: return [-1,-1]
        return [first,sec-1]
