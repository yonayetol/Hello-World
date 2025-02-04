class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s,t,ans = Counter(s),Counter(t),0

        for i,c in t.items():
            if c > s[i]:
                ans += c - s[i]
                
        return ans