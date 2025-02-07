class Solution:
    def romanToInt(self, s: str) -> int:
        my_dict = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        runing = 0
        for i in range(len(s)):
            runing += my_dict[s[i]]
            if i > 0 and my_dict[s[i]] > my_dict[s[i-1]]:
                runing -= 2*my_dict[s[i-1]]
        return runing
