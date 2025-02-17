class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        negative = False
        left, right = 0, len(s)
        if len(s) == 0:
            return 0
        if s[left] == "-" or s[left] == "+":
            if s[left] == "-":
                negative = True
            left += 1

        elif not s[left].isdigit():
            return 0

        while left < right:
            if s[left] != 0:
                break
            left += 1

        for i in range(left,right):
            if not s[i].isdigit():
                right = i
                break

        if left == right:
            return 0

        answer = int(s[left:right])
        if negative:
            answer *= -1
            answer = max(-1*(2**31),answer)
        else:
            answer = min(answer, 2**31 - 1)
        return answer