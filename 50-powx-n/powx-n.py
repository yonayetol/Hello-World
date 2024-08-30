class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            n,x = -n,1/x
        def other(x,n):
            if n == 0:
                return 1
            even = (n%2 == 0)
            if even:
                return other(x,n//2)**2
            else:
                return other(x,n//2)**2*x
        return other(x,n)