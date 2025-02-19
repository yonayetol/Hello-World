class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        paired = sorted(list(zip(nums, cost)), key = lambda x: (x[0],x[1]))
        n = len(paired)
        suffix_operation = [0]*(len(nums))
        total_cost = paired[n-1][1]
        for i in range(n-2,-1,-1):
            num , price = paired[i]
            suffix_operation[i] = suffix_operation[i+1] + (paired[i+1][0] - num)*total_cost
            total_cost += paired[i][1]
        
        total_cost = 0
        tempo = 0
        for i in range(n):
            num, price = paired[i]
            if i > 0: tempo = paired[i-1][0] + (num-tempo)*total_cost
            prev_num = paired[i][0]
            paired[i] = tempo,paired[i][1]
            total_cost += paired[i][1]
            tempo = prev_num
            
        minimum = float('inf')
        for i in range(n):
            minimum = min(minimum,paired[i][0]+suffix_operation[i])
        return minimum