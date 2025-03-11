class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        ans = log(n,4)
        if ans != ceil(ans):
            return False
        return True