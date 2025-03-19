class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        answer = deque()
        for num in sorted(deck, reverse = True):
            if answer: answer.appendleft(answer.pop())
            answer.appendleft(num)
        return list(answer)