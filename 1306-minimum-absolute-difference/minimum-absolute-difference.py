class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mini, n = float('inf'), len(arr)
        for i in range(n-1): mini = min(mini, arr[i+1]-arr[i])
        i, answer = 0, []
        # 1 2 3 4   {1}
        for i in range(n):
            j = i+1
            while j < n and arr[j]-arr[i]<=mini:
                answer.append([arr[i],arr[j]])
                j += 1
        return answer