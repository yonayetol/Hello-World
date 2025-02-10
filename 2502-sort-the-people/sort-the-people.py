class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ans = list(zip(heights,names))

        for i in range(len(names)):
            for j in range(i+1,len(names)):
                if ans[i][0] < ans[j][0]:
                    ans[i], ans[j] = ans[j], ans[i]
        return [sub[1] for sub in ans]