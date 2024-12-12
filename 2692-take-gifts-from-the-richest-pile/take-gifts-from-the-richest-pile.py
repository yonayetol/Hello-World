class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        for i in range(k):
            maxiat = 0
            for j in range(len(gifts)):
                if gifts[j] > gifts[maxiat]:
                    maxiat = j
            gifts[maxiat] = int(gifts[maxiat]**0.5)
        return sum(gifts) 