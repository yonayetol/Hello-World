class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans,maxi = 0,0
        for i in range(len(mat)):
            mat[i] = sum(mat[i])
            if mat[i] > maxi:
                maxi, ans = mat[i], i
        return [ans, maxi]
        