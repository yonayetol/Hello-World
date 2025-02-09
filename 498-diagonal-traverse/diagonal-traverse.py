class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        answer = []
        row,column = len(mat),len(mat[0])
        ptr1,ptr2 = 0,0
        going_up = True
        while len(answer) < row*column :
            answer.append(mat[ptr1][ptr2])
            if going_up:
                if ptr1 == 0 or ptr2 == column-1:
                    going_up = False
                else:
                    ptr1 -= 1

                if ptr2 + 1 < column:
                    ptr2 += 1
                else:
                    ptr1 += 1

            else:
                if ptr1 == row-1 or ptr2 == 0:
                    going_up = True
                else:
                    ptr2 -= 1

                if ptr1 + 1 < row:
                    ptr1 += 1
                else:
                    ptr2 += 1
        return answer