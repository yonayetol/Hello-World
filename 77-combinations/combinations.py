class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        def helper(i, arr):
            arr.append(i)
            if len(arr) == k:
                answer.append(arr[:])
                arr.pop()
                return

            for j in range(i+1,n+1):
                helper(j,arr)
            arr.pop()

        for i in range(1, n-k+2):
            helper(i,[])
        return answer