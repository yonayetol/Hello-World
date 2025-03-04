class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        tempo = 3**16

        while tempo > 0:
            while n - tempo < 0:
                tempo //= 3
            n -= tempo
            tempo //= 3
            
        return n == 0 