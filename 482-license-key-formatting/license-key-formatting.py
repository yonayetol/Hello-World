class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        newS = ""
        for char in s:
            if char == "-": continue
            newS += char.upper()

        firstGrp = len(newS) % k
        firstGrp = firstGrp if firstGrp else k

        answer = ""
        idx = 0

        miniK = firstGrp
        while idx < len(newS):
            miniK -= 1
            answer += newS[idx]
            if miniK == 0:
                miniK = k
                answer += "-"
            idx += 1

        return answer[:-1]