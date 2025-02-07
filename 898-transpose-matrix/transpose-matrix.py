class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        column = len(matrix[0])
        answer = [[0 for _ in range(row)] for _ in range(column)]

        for i in range(row):
            for j in range(column):
                answer[j][i] = matrix[i][j]
        return answer