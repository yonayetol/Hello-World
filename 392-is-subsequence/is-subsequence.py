class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sInd = 0
        if sInd == len(s) or len(t) == 0 == len(s): return True
        for i in range(len(t)):
            if t[i]==s[sInd]: 
                sInd += 1
                if sInd == len(s): return True
        return False