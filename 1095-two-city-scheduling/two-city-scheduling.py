class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: (x[0]-x[1]))
        n = len(costs)
        total = 0
        for i in range(n//2):
            total += min(costs[i][0] + costs[n-i-1][1], costs[i][1] + costs[n-i-1][0])
        return total