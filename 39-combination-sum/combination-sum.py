class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        tempo = []
        # candidates.sort()
        def backTrack(i,currSum):
            for j in range(i,len(candidates)):
                tempo.append(candidates[j])
                currSum += candidates[j]
                if currSum == target:
                    answer.append(tempo.copy())
                if currSum < target:
                    backTrack(j,currSum)
                
                tempo.pop()
                currSum -= candidates[j]

        backTrack(0,0)
        return answer