class Solution:
    def clearDigits(self, s: str) -> str:
        answer = ""
        the_list = []

        i = len(s)-1
        count = 0
        while i > -1:
            if s[i].isdigit():
                count += 1
            if s[i].isalpha():
                if count == 0:
                    the_list.append(s[i])
                elif count > 0:
                    count -= 1
            i -= 1
        
        return "".join(the_list[::-1])