class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        ans = nums[0]
        while l + 1  < r:
            mid = l + (r-l) // 2

            if nums[mid] <= nums[r]:
                r = mid
                # ans = nums[mid]
            else:
                l = mid

        return min(nums[r], nums[l])
        
        
