class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)//3
        total = 0
        for i in range(3*n-2,n-1,-2):
            total += piles[i]
        return total