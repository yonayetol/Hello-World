class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxxi = 0
        for sub in accounts:
            maxxi = max(maxxi,sum(sub))
        return maxxi