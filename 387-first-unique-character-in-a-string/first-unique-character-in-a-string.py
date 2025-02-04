class Solution:
    def firstUniqChar(self, s: str) -> int:
        mine = Counter(s)
        for i in range(len(s)):
            if mine[s[i]] == 1:
                return i
        return -1