class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        answer,ptr = 0,0
        while ptr < len(costs) and costs[ptr] <= coins:
            coins -= costs[ptr]
            answer += 1
            ptr += 1
             
        return answer