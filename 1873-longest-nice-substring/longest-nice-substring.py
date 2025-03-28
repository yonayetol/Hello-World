class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def divide(s):
            if len(s) < 2: return "" # basecases

            myset = set(s)
            for i,char in enumerate(s):
                opposite_case = char.swapcase()
                if opposite_case not in myset:
                    left = divide(s[:i])
                    right = divide(s[i+1:])
                    return left if len(left)>=len(right) else right
            return s
        return divide(s)