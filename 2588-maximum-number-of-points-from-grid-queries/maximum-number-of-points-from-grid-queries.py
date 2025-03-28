import heapq
from typing import List

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        M, N = len(grid), len(grid[0])
        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])
        ans = [0] * len(queries)
        
        heap = []
        visited = [[False] * N for _ in range(M)]
        count = 0
        
        heapq.heappush(heap, (grid[0][0], 0, 0))
        visited[0][0] = True
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for threshold, qi in sorted_queries:
            while heap and heap[0][0] < threshold:
                val, i, j = heapq.heappop(heap)
                count += 1
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < M and 0 <= nj < N and not visited[ni][nj]:
                        visited[ni][nj] = True
                        heapq.heappush(heap, (grid[ni][nj], ni, nj))
            ans[qi] = count
        return ans