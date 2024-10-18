class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x = num**0.5
        if x == int(x):
            return True
        return False