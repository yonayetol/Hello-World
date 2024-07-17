class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        final = []
        while n>0:
            remainder=n%2
            final.insert(0,remainder)
            n//=2
        def palindrome_checker(take):
            red = []
            for n in range(len(final)-1,-1,-1):
                red.append(n)
            if red==take:
                return True
            return False
        n=0
        while len(final)>0:
            response = palindrome_checker(final)
            if response==False:
                return False
            final = final[:-n]
            n+=1
        return True
            