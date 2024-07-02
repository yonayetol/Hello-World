class Solution:
    def romanToInt(self, s: str) -> int:
        my_dict={
                    "I":1,
                    "V":5,
                    "X":10,
                    "L":50,
                    "C":100,
                    "D":500,
                    "M":1000,
                }
        final=[my_dict[char] for char in s]
        sum=final[-1]
        for n in range(len(s)-1):
            sum+=final[n]
            if final[n]<final[n+1]:
                sum-=(final[n]*2)
        return sum