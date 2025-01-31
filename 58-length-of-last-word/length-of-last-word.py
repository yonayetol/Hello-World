class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = ""
        for i in range(len(s)-1,-1,-1):
            if ans != "" and s[i] == " ":
                return len(ans)
            if s[i] != " ":
                ans += s[i]
        return len(ans)