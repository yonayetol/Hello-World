class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def good(rate):
            totalTime = 0
            for i in range(len(piles)):
                totalTime += ceil(piles[i]/rate)
                if totalTime > h: return False
            return True
        
        left = ans = 1
        right = max(piles)
        while left <= right:
            mid = (left+right)//2
            if good(mid):
                ans = mid
                right = mid - 1
            else: left = mid + 1

        return ans