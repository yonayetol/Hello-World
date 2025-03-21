class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        if nums[0]==nums[-1]==0:return 0
        posptr = (len(nums))//2 -1
        def pos_track(posptr,n):
            n = ceil(n/2)            
            if nums[posptr] > 0:
                if posptr <= 0 or nums[posptr-1] <=0:
                    return max(0,posptr)
                return pos_track(posptr-n,n)
            else:
                if posptr >= len(nums)-1 or nums[posptr + 1] > 0:
                    return min(len(nums)-1,posptr + 1)
                return pos_track(posptr + n,n) 

        def neg_track(posptr,n):
            n = ceil(n/2)
            if nums[posptr] < 0:
                if posptr >= len(nums)-1 or nums[posptr+1] >=0:
                    return min(posptr,len(nums)-1)
                return neg_track(posptr + n,n)   
            else:
                if posptr <= 0 or nums[posptr - 1] < 0:
                    return max(posptr - 1,0)
                return neg_track(posptr - n, n)
                
        return max(len(nums)-pos_track(posptr, ceil(len(nums)/2)),1+neg_track(posptr, ceil(len(nums)/2)))
