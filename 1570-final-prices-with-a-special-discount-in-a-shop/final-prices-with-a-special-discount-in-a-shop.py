class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []      
        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                prices[stack[-1]] -= prices[i]
                stack.pop()
            stack.append(i)
        return prices