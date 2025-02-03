class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split(" ")
        def mine(word):
            return len(word)

        maxi = len(max(s,key = mine))
        my_dict = {i:"" for i in range(maxi)}

        for sub in s:
            for i in range(maxi):
                if i >= len(sub):
                    my_dict[i] += " "
                else:
                    my_dict[i] += sub[i]
        
        return [word.rstrip() for word in my_dict.values()]
        