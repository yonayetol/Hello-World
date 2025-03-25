class Solution:
    def search(self, nums: List[int], target: int) -> int:        
        left,right = 0,len(nums)-1
        mid = (left+right)//2

        while mid != right:
            if nums[mid] == target: return mid
            elif nums[mid] > target: right = mid - 1
            else: left = mid + 1

            mid = (left+right)//2

        return mid if nums[mid] == target else -1