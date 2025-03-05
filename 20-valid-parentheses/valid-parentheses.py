class Solution:
    def isValid(self, s: str) -> bool:
        stack,pairs = [],{"(":")","{":"}","[":"]"}
        for i in range(len(s)):
            if stack and stack[-1] in pairs and pairs[stack[-1]] == s[i]:
                stack.pop()
            elif stack and stack[-1] not in pairs:
                return False
            else:
                stack.append(s[i])
        return not stack
