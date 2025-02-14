class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxs = [set() for i in range(9)]
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    num = int(num)
                    if num in rows[i]:
                        return False
                    rows[i].add(num)

                    if num in cols[j]:
                        return False
                    cols[j].add(num)

                    for_box = (i//3 * 3) + j//3
                    if num in boxs[for_box]:
                        return False
                    boxs[for_box].add(num)
        return True
                    
