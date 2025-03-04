class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[0])                                                           
        count = i = 0
        while i < len(points):
            starter = points[i][1]
            while i < len(points) and points[i][0] <=  starter:
                starter = min(starter,points[i][1])
                i += 1

            count += 1
        return count