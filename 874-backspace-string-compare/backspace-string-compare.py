class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def correcter(word):
            stack = []
            for char in word:
                if char != "#":
                    stack.append(char)
                elif stack:
                    stack.pop()
            return stack
        return correcter(s)==correcter(t)