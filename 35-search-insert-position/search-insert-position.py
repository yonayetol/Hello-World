class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        mine=nums[:]
        if target in nums:
                return nums.index(target)
        elif target>nums[-1]:
            return len(nums)
        elif target < nums[0]:
            return 0
        for mo in range(len(mine)//2):
            print(mine)
            n=len(mine)//2 
            if mine[n]<target:
                if mine[n+1]>target>mine[n]:
                    return nums.index(mine[n+1])
                mine=mine[n:]
            else:
                if mine[n]>target>mine[n-1]:
                    return nums.index(mine[n])
                mine=mine[:n]