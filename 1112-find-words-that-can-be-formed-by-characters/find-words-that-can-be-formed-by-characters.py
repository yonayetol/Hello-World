class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        new_chars = Counter(chars)
        runing = 0
        for word in words:
            if Counter(word) <= new_chars:
                runing += len(word)

        return runing