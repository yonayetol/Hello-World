class Solution:
    def isValid(self,s: str) -> bool:
        symbol_list=[]
        try:
            for n in range(len(s)):
                if s[n]=="[" or s[n]=="(" or s[n]=="{":
                    symbol_list.append(f"{s[n]}")
                if s[n]=="]":
                    if symbol_list[-1]!="[":
                        return False
                    symbol_list.pop()
                if s[n]==")":
                    if symbol_list[-1]!="(":
                        return False
                    symbol_list.pop()
                if s[n]=="}":
                    if symbol_list[-1]!="{":
                        return False
                    symbol_list.pop()
            if len(symbol_list)!=0:
                return False
            return True
        except:
            return False