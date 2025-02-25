class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        tempo = count = 0

        for i in range(n):
            tempo += arr[i]
            if tempo % 2 == 1:
                count += 1 
        
        tempo = count # re-use      
        for i in range(1,n):         
            if arr[i-1] % 2 == 1:
                tempo = (n-(i-1)-tempo)
                
            count += tempo
        return count%(10**9 + 7)

        # Brute force is this one, but cannot pass due to the constraint
        # count = 0
        
        # runing = 0
        # for j in range(i,len(arr)):
        #     runing += arr[j]
        #     if runing % 2 == 1:
        #         count += 1
        
        # n = (len(arr))*(len(arr)+1)//2

        # return count
