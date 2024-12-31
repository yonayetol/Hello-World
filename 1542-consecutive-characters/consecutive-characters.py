class Solution:
    def maxPower(self, s: str) -> int:
        mine = {}
        lft = 0
        answer = 1
        for i in range(1,len(s)):
            answer = max(i-lft, answer)
            if s[i] != s[lft]:
                lft = i
        answer = max(len(s)-lft, answer)
        return answer