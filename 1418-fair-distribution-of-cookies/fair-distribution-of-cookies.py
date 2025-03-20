class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        if k == len(cookies): return max(cookies)
        children = [0]*k
        fairness = float('inf')
        def backTrack(i,children):
            nonlocal fairness
            nums = max(children)
            if i == len(cookies):
                fairness = min(fairness, nums)
                return 
            if nums > fairness: return 
            
            for j in range(k):
                children[j] += cookies[i]
                backTrack(i+1 , children)
                children[j] -= cookies[i]
        
        backTrack(0,children)
        return fairness
        
