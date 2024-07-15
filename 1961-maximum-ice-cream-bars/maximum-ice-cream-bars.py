class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        finals = 0
        costs=sorted(costs)
        for i in costs:
            if coins>=i:
                coins-=i
                finals+=1
            else:
                break
        return finals