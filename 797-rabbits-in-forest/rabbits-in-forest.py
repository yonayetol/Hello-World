class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter,count = Counter(answers), 0
        for color, many in counter.items():
            count += (color + 1)*(ceil(many / (color + 1)))
        return count