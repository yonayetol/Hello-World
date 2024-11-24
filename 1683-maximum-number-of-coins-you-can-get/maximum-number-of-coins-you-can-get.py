class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        repeating_times = range(int(len(piles)/3)) 
        piles.sort()
        Mine_coin,x = 0,-2
        for i in repeating_times:
            Mine_coin += piles[x] 
            x -= 2
        return Mine_coin
        # 1 2 2 4 7 8
        # 7 2