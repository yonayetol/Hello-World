from collections import deque
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        ourSet = set()
        run = deque(s[:k])
        ourSet.add(tuple(run))
        for i in range(k,len(s)):
            run.popleft()
            run.append(s[i])
            ourSet.add(tuple(run))         
            
        return len(ourSet) == 2**k