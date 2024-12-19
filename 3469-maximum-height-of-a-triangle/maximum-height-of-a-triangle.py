class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        a,count,max_col,min_col = 0,0,max(red,blue),min(red,blue)
        
        while True:
            a += 1
            if max_col - a >= 0:
                max_col -= a
                count += 1
            else:
                break
            a += 1
            if min_col - a >= 0:
                min_col -= a
                count += 1
            else:
                break
        tempo = count
        max_col,min_col = min(red,blue),max(red,blue)
        count,a = 0,0
        while True:
            a += 1
            if max_col - a >= 0:
                max_col -= a
                count += 1
            else:
                break
            a += 1
            if min_col - a >= 0:
                min_col -= a
                count += 1
            else:
                break
        return max(tempo,count)

            
            