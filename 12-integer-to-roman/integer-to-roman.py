class Solution:
    def intToRoman(self, num: int) -> str:
        my_dict={
            1:"I",
            5:"V",
            10:"X",
            50:"L",
            100:"C",
            500:"D",
            1000:"M"
        }
        new_list=list(str(num))
        final=""
        for i in range(len(new_list)):
            new_i=int(new_list[i])
            mana=10**(len(new_list[i+1:]))
            if new_i < 4:
                final+=(my_dict[mana]*new_i)
            elif new_i==4:
                final+=my_dict[mana]+my_dict[mana*5]
            elif new_i==5:
                final+=(my_dict[mana*5])
            elif new_i<9:
                final+=my_dict[mana*5]+my_dict[mana]*(new_i-5)
            elif new_i==9:
                final+=my_dict[mana]+my_dict[mana*10]
        return final