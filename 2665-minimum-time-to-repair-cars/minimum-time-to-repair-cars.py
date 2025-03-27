class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def isGood(minute):
            fixedCar = 0
            for rank in ranks:
                fixedCar += floor(sqrt(minute/rank))
                if fixedCar >= cars: return True

            return False
        
        minMinute, maxMinute = 0, (cars**2)*ranks[0]
        while minMinute <= maxMinute:
            mid = (minMinute + maxMinute)//2
            if isGood(mid):
                maxMinute = mid - 1
            else:
                minMinute = mid + 1
        return minMinute
