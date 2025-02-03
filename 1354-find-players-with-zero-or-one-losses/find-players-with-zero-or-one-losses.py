class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losers = Counter()
        win = set()
        for sub in matches:
            losers[sub[1]] += 1
            win.add(sub[0])
        only_win = sorted([i for i in win if losers[i] == 0])
        only_1_lose = sorted([i for i,c in losers.items() if c == 1])
        return [only_win,only_1_lose]
