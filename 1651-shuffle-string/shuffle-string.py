class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        new_list = [0]*101
        for i in range(len(indices)):
            new_list[indices[i]] = s[i]
        answer = ""
        for char in new_list:
            if char != 0:
                answer += char
        return answer