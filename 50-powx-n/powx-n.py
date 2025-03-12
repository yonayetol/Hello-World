class Solution:
    def myPow(self, x: float, n: int) -> float:
        reminder = {}
        def other(x,m):
            if m == 0: return 1
            if m == 1: return x

            if ceil(m/2) not in reminder: reminder[ceil(m/2)] = other(x,ceil(m/2))
            if m//2 not in reminder: reminder[m//2] = other(x,m//2)
                
            return reminder[ceil(m/2)] * reminder[m//2]

        ans = other(x,abs(n))
        if n < 0:
            return 1/ans
        return ans