class Solution:
    def trailingZeroes(self, n: int) -> int:
        def factorial(num):
            if num <= 1:
                return 1
            return factorial(num-1) * num
        ans = factorial(n)
        if n < 10 :print(ans)
        count = 0
        while True:
            last = ans%10
            if last != 0:
                return count
            ans //= 10
            count += 1