class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        answer = 0
        for char in operations:
            if "++" in char:
                answer += 1
            else:
                answer -= 1
        return answer