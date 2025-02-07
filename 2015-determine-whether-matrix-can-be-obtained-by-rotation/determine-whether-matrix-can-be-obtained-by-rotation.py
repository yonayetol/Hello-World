class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if target == mat:
            return True
        new_created = deepcopy(target)
        n = len(mat)
        for _ in range(3):
            for i in range(n):
                for j in range(len(mat)):
                    new_created[i][j] = mat[n-j-1][i]
            if target == new_created:
                return True
            mat = deepcopy(new_created)
            print(mat)
        return False


            