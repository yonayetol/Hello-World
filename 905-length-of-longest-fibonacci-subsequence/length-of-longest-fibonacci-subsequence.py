class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        store,n,count = {arr[i]:i for i in range(len(arr))}, len(arr),0
        
        for i in range(n-1):
            j = i + 1
            while j < n:
                first,sec,tempo, eegdu = arr[i], arr[j], 2, j
                while j < n and first + sec in store:
                    tempo += 1
                    j,first = store[first + sec],sec
                    sec, count = arr[j], max(count, tempo)
                    
                j = eegdu + 1
        return count