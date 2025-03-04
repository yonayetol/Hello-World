class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        while target > 1:
            if maxDoubles == 0: return target - 1 + count

            if target % 2: target -= 1
            else:
                target //= 2
                maxDoubles -= 1

            count += 1
            
        return count