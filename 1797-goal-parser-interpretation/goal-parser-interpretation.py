class Solution:
    def interpret(self, command: str) -> str:
        mine = {"(al)":"al","G":"G","()":"o"}
        tempo,answer = "",""
        for char in command:
            tempo += char
            if tempo in mine:
                answer += mine[tempo]
                tempo = ""
        return answer