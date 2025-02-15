class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        intersections = []
        
        while i < len(A) and j < len(B):
            start_max = max(A[i][0], B[j][0])
            end_min = min(A[i][1], B[j][1])
            if start_max <= end_min:
                intersections.append([start_max, end_min])
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        
        return intersections