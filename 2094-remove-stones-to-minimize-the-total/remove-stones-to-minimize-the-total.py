from heapq import heappop, heappush, heapify
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)): piles[i] *= (-1)

        heapify(piles)

        for i in range(k):
            theBigNum = heappop(piles)
            heappush(piles, floor(theBigNum/2))
        
        return sum(piles)*(-1)