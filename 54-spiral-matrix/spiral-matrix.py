class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        answer = []
        top,right,bottom,left = 0,len(matrix[0])-1,len(matrix)-1,0
        at_the_end = len(matrix[0]) * len(matrix)
        while at_the_end != len(answer):
            answer.extend(matrix[top][left:right+1])
            top += 1 # for the top part
            if at_the_end == len(answer):
                return answer
            
            answer.extend([matrix[i][right] for i in range(top,bottom+1)])
            right -= 1 # for the right part
            if at_the_end == len(answer):
                return answer
            
            if left == 0:
                answer.extend(matrix[bottom][right::-1])
            else:
                answer.extend(matrix[bottom][right:left-1:-1])
            bottom -= 1# for the bottom one 
            if at_the_end == len(answer):
                return answer

            answer.extend([matrix[i][left] for i in range(bottom,top-1,-1)])
            left += 1# for the left part
        return answer
                
            