class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(i,rightNumber):
            if rightNumber < 0: return False
            num = 0
            while i < len(s) and (num < rightNumber or int(s[i])==0==num):
                num = num * 10 + int(s[i])
                i += 1

            if num == rightNumber:
                if i == len(s): return True
                return backtrack(i, rightNumber-1)
            return False

        numx = 0
        for i in range(len(s)-1):
            numx = numx*10 + int(s[i])
            if backtrack(i+1,numx-1):
                return True

        return False

        