class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        answer, tempList, temp = [], [], 0
        poped = float('inf')
        
        def backTrack(i):
            nonlocal temp, poped
            for j in range(i,len(candidates)):
                if poped != candidates[j]:
                    tempList.append(candidates[j])
                    temp += candidates[j]

                    if temp == target and (len(answer)==0 or(len(answer) > 0 and answer[-1] != tempList)):
                        answer.append(tempList[:])
                    if temp < target: backTrack(j+1)

                    poped = tempList.pop()
                    temp -= candidates[j]

        backTrack(0)
        return [list(sub) for sub in answer]