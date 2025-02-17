class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        def inbound(r,c):
            if  0 <= r < len(matrix) and 0 <= c < len(matrix[0]):
                return self.matrix[r][c]
            return 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.matrix[i][j] += inbound(i-1 , j) + inbound(i , j-1) - inbound(i-1 , j-1)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        def inbound(r,c):
            if  0 <= r < len(self.matrix) and 0 <= c < len(self.matrix[0]):
                return self.matrix[r][c]
            return 0
        return self.matrix[row2][col2] + inbound(row1-1,col1-1) - inbound(row1-1,col2) - inbound(row2,col1-1)

