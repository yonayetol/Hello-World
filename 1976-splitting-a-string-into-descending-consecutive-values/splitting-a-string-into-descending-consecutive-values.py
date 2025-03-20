class Solution:
    def splitString(self, s: str) -> bool:
        def splitter(path, i):
            if i == len(s):
                for j in range(1,len(path)):
                    if path[j] + 1 != path[j-1]: return False
                return len(path) >= 2
            
            num = 0
            for j in range(i,len(s)):
                num = num*10 + int(s[j])
                path.append(num)
                if splitter(path,j+1): return True
                path.pop()
            return False

        return splitter([],0)

        # s = s.lstrip("0")
        # def backtrack(i,rightNumber,tempo):
        #     num = 0
        #     while i < len(s) and num < rightNumber:
        #         # width increases
        #         tempo.append(s[i])
        #         i += 1
        #         num = int("".join(tempo))
        #         print("i is now ",i,"and tempo is ",tempo)
        #     if num == rightNumber:
        #         if i == len(s): return True
                
        #         backtrack(i+1, rightNumber-1,[])

        #     if num > rightNumber:
        #         return False
 
        # for i in range(len(s)):
        #     if backtrack(i+1,int(s[:i+1])-1,[]):
        #         return True

        #     print(int(s[:i+1]),i)

        # return False

        