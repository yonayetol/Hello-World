class Solution:
    def balancedStringSplit(self, s: str) -> int:
        # as soon as we get equal number of R and L group them in order to get maximum valid groups
        R = count = 0
        for char in s:
            R += 1 if char == "R" else -1 
            if R == 0: count += 1

        return count