class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        lft,count,answer = 0,1,0

        for i in range(1,len(nums)):
            answer = max(answer,count)
            if nums[i]-nums[lft] <= 2*k:
                count += 1
            while nums[i]-nums[lft] > 2*k:
                lft += 1
                count -= 1
                if nums[i]-nums[lft] <= 2*k:
                    count += 1

        return max(answer,count)
                
            