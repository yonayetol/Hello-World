class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        difference,count = [0]*(len(nums)+1),0
        for x,y in requests:
            difference[x] += 1
            difference[y+1] -= 1
        for i in range(1,len(difference)):difference[i] += difference[i-1]

        difference.sort()
        nums.sort()
        
        for i in range(1,len(difference)):count += difference[i]*nums[i-1]
            
        return count % (10**9 + 7)