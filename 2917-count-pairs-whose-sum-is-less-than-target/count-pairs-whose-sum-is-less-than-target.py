class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count, other = 0, [0]*102 
        for i in nums:
            other[i+50] += 1
        nums.clear()
        for i in range(len(other)):
            if other[i] != 0:
                nums.extend(([i-50]*other[i]))
        lft,rgt = 0,len(nums)-1
        while lft < rgt:
            if nums[lft] + nums[rgt] < target:
                count += rgt - lft
                lft += 1
            else:
                rgt -= 1
        return count 
        