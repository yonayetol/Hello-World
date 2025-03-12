class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def ReverseInverse(n, s):
            inverse = []
            for char in s[::-1]:
                if char == "0":
                    inverse.append("1")
                else:
                    inverse.append("0")

            return s + "1" + "".join(inverse)

        tempo = "0"
        for i in range(1,n):
            tempo = ReverseInverse(i, tempo)
        return tempo[k-1]