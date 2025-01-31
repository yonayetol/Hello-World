class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        empty = 0
        answer = 0
        while numBottles > 0:
            answer += numBottles
            empty += numBottles
            if empty >= numExchange:
                numBottles = (empty//numExchange)
                empty = empty % numExchange
            else:
                numBottles = 0
        return answer