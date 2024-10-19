class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        x,final = 0,0
        for i in range(len(s)):
            if x<len(g) and s[i] >= g[x]:
                final += 1
                x += 1
        return final