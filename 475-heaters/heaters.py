class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        def isvalid(standardRadius):
            ptr = 0
            for section in houses:
                while ptr < len(heaters) and abs(section-heaters[ptr]) > standardRadius:
                    ptr += 1
            return ptr<len(heaters)

        left = 0
        right = max(houses[-1], heaters[-1])
        while left <= right:
            mid = (left+right)//2
            if isvalid(mid): right = mid - 1
            else: left = mid + 1
        return left