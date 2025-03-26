class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = sorted([item for sub in grid for item in sub])
        half = len(arr)//2

        def helper(start, end, inc):
            running, ptr = 0, 1
            for i in range(start,end,inc):
                gap = abs(arr[i]-arr[i-inc])
                if gap % x != 0: return -1
                running += ptr*gap//x
                ptr += 1
            return running

        forward =  helper(1 , half+1 , 1)
        if forward == -1:return -1 
        backward = helper(len(arr)-2 , half-1 , -1)
        if backward == -1: return -1
    
        return forward+backward