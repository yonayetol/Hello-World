class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            for j in range(i,n-1-i): # 00 to 02  to 22 to 20
                a = matrix[i][j]
                b = matrix[j][n-1-i]
                c = matrix[n-1-i][n-1-j]
                d = matrix[n-1-j][i] 
                matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j], matrix[n-1-j][i] = d, a, b, c
        return matrix
        