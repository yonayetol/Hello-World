class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def helper(arr, ptr):
            maxi = float('-inf')
            lines = -1
            for sub in arr:
                if sub[ptr] >= maxi: 
                    lines += 1
                    if lines == 2: return True

                maxi = max(sub[ptr+2], maxi)

            return False 

        return helper(sorted(rectangles, key = lambda sub: (sub[0], -sub[2])),0) or helper(sorted(rectangles, key = lambda sub: (sub[1], -sub[3])),1)