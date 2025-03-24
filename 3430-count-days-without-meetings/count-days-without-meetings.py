class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        hash = Counter()
        for sub in meetings:
            hash[sub[0]] += 1
            hash[sub[1]+1] -= 1
        
        gameChangerDays = [[num, hash[num]] for num in sorted(hash.keys())]
        for day in range(1,len(gameChangerDays)):
            gameChangerDays[day][1] += gameChangerDays[day-1][1]
            
        total = gameChangerDays[0][0]-1
        left = 0 
        for right in range(1,len(gameChangerDays)):
            if gameChangerDays[right][1] > 0 and gameChangerDays[right-1][1] == 0:
                total += gameChangerDays[right][0]-gameChangerDays[right-1][0]

        total = max(total + days-gameChangerDays[right][0]+1, total)
        if gameChangerDays[right][1] > 0:
            total -= 1
        return total

        