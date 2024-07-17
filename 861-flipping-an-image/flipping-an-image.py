class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:       
        final=[]
        for t in image:
            new = []
            for i in range(len(t)-1,-1,-1):
                if t[i] == 0:
                    t[i]=1
                else:
                    t[i]=0
                new.append(t[i])
            final.append(new)
        return final