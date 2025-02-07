class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        column = len(matrix[0])
        answer = []
        for i in range(column):
            answer.append([])
            for j in range(row):
                answer[i].append(0)

        for i in range(row):
            for j in range(column):
                answer[j][i] = matrix[i][j]
        return answer