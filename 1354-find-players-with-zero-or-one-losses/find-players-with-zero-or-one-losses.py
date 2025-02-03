class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wins = set()
        lost = Counter()

        for winner,loser in matches:
            wins.add(winner)
            lost[loser] += 1

        array1 = []
        array2 = []
        for player in wins:
            if player not in lost:
                array1.append(player)
        array1.sort()

        for player in lost:
            if lost[player] == 1:
                array2.append(player)
        array2.sort()
        return [array1,array2]
