class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ptrs, ptrt = len(s)-1, len(t)-1
        while  ptrs > -1 or ptrt > -1:
            count = 0
            while ptrs > -1 and (count > 0 or s[ptrs] == "#"):
                count += 1 if s[ptrs] == "#" else -1
                ptrs -= 1

            count = 0
            while ptrt > -1 and (count > 0 or t[ptrt] == "#"):
                count += 1 if t[ptrt] == "#" else -1
                ptrt -= 1
                
            if ptrs != -1 and ptrt != -1 and t[ptrt] == s[ptrs]:
                ptrs -= 1
                ptrt -= 1
            elif (ptrs <= -1 and ptrt != -1) or (ptrs != -1 and ptrt <= -1) or (ptrs!=-1 and ptrt!= -1 and s[ptrs] != t[ptrt]): return False

        return True
