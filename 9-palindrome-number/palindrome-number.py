class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        new = str(x)
        if new == new[::-1]:
            return True
        return False