class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def checker(i):
            if i == 1: return False
            for j in range(2, int(i**0.5)+1):
                if i % j == 0: return False
            return True
        
        ans, final = [], [-1 , -1]
        while left <= right + 1:
            if len(ans) > 1 and (final[1] - final[0] == 0  or ans[-1] - ans[-2] < final[1] - final[0]):
                final = [ans[-2] , ans[-1]]
                ans = [ans[-2] , ans[-1]]
                if final[1] - final[0] < 3: return final
                
            if checker(left):
                if len(ans) > 1 and ans[1] - ans[0] < left - ans[-1]:
                    ans.pop()
                ans.append(left)

            left += 1
        if len(ans) > 1 and final[1] - final[0] > ans[-1] - ans[-2]:
            final = [ans[-2], ans[-1]]
        return final