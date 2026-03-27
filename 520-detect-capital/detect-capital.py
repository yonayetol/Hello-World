class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word[0].isupper(): return len(word)<2 or (word[1].isupper() and word[1:].upper()==word[1:]) or (word[1].islower() and word[1:].lower()==word[1:])
        else: return word.lower()==word