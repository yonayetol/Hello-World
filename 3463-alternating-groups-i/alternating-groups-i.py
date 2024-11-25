class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        x,new,ptr,count = len(colors),[],3,0

        for i in range(x):
            while len(new)<3:
                if ptr == x:
                    ptr = 0
                new.append(colors[ptr])
                ptr += 1                
            if new == [0,1,0] or new == [1,0,1]:
                count += 1
            new.pop(0)
        return count

        
