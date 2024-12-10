class Solution:
    def maximumLength(self, s: str) -> int:
        dict_name,answer = {},-1
        def dict_adder(special_sub_str):
            tempo = ""
            length = len(special_sub_str)
            for i in range(length):
                tempo += special_sub_str[i]
                if tempo not in dict_name:
                    dict_name[tempo] = 0
                dict_name[tempo] += length-i

        tempo,length = "",len(s)
        for i in range(length):
            if (len(tempo)>0 and tempo[0] != s[i]):
                dict_adder(tempo)
                tempo = s[i]
            else:
                tempo += s[i]
        dict_adder(tempo)
        
        for x,y in dict_name.items():
            if y > 2:
                answer = max(answer,len(x))
        return answer