class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def good(maxiLoad):
            countDays = 0
            totalload = 0
            for i in weights:
                if i > maxiLoad: return False
                totalload += i
                if totalload > maxiLoad:
                    countDays += 1
                    totalload = i
                
            return countDays+1 <= days
            
        minLoad = 1
        maxLoad = 10**18
        while minLoad <= maxLoad:
            mid = (minLoad+maxLoad)//2
            if good(mid):
                maxLoad = mid - 1
            else:
                minLoad = mid + 1
        return minLoad