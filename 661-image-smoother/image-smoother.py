class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        moves = [(-1,-1),(-1,0),(-1,1),(0,1),(0,-1),(1,1),(1,0),(1,-1)]
        n = len(img)
        m = len(img[0])
        answer = [[0]*m for i in range(n)]

        for i in range(n):
            for j in range(m):
                little_sum = img[i][j]
                count = 1
                for x,y in moves:
                    if 0<=i+x<n and 0<=j+y<m:
                        count += 1 
                        little_sum += img[i+x][j+y]
                answer[i][j] = little_sum//count
        return answer