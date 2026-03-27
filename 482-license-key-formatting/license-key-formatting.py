class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        newS = s.replace("-","").upper()

        firstGrp = len(newS) % k or k
        
        answer = newS[:firstGrp] + "-"
        idx = firstGrp

        while idx < len(newS):
            answer += newS[idx:idx+k]
            answer += "-"
            idx += k

        return answer[:-1]