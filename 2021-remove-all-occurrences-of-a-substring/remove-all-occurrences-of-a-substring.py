class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        part = [char for char in part]
        n = len(part)
        stack = []

        for i in range(len(s)):
            stack.append(s[i])
            while len(stack) >= n and stack[-n:] == part:
                for _ in range(n):
                    stack.pop()
                    
        return "".join(stack)