class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        letters = [[chr(i),0] for i in range(97, 123)]
        count = 0
        for char in s:
            for i in range(len(letters)):
                if letters[i][0] == char:
                    letters[i][1] += 1
                    break
        
        for i in range(26):
            if letters[i][1] != 0:
                count = letters[i][1] 
                break

        for i in range(len(letters)):
            if letters[i][1] != 0:
                if letters[i][1] != count:
                    return False

        return True