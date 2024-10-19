class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        chosen = {}
        for i,e in enumerate(score):
            chosen[e[k]] = i
        chosen = sorted(chosen.items())
        new = []
        for i,e in chosen:
            new.append(score[e])
        new.reverse()
        return new
                