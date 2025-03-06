class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        stack = []
        for i in range((len(temperatures))):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                ind = stack.pop()
                ans[ind] = i - ind
            stack.append(i)
        return ans