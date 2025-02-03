class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
        ranges.sort()
        while left <= right:
            for sub in ranges:
                if sub[0] <=left and left <= sub[1]:
                    left = sub[1] + 1
                    break
            else:
                return False
        return True
                