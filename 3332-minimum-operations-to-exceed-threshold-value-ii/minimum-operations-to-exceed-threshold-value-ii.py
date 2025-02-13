class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        count,x = 0,0
        y = len(nums)
        x = heappop(nums)
        while y>1 and x<k:
            y = heappop(nums)
            heappush(nums, x*2 + y)
            count += 1
            y = len(nums) # wise use of y to control the length and be the criteria
            x = heappop(nums)
        return count