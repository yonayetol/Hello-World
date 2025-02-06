class Solution:
    def intToRoman(self, num: int) -> str:
        my_dict = {
            1:"I",
            4:"IV",
            5:"V",
            9:"IX",
            10:"X",
            40:"XL",
            50:"L",
            90:"XC",
            100:"C",
            400:"CD",
            500:"D",
            900:"CM",
            1000:"M",
        }
        def mine(elem):
            if elem != "0":
                return int(elem)
            return ""
        new = list(map(mine, str(num)))
        n = len(new)

        for i in range(n):
            factor = (10**(n-i-1))
            if new[i] == 9 or new[i] == 4 or new[i] == 1 or new[i] == 5:
                new[i] = my_dict[(new[i] * factor)]

            elif new[i] != "" and new[i] > 5:
                new[i] = my_dict[5*factor] + (new[i] - 5)*my_dict[factor]

            elif new[i] != "" and new[i] > 0:
                new[i] = new[i]*(my_dict[factor])
            
        return"".join(new)

                
    
