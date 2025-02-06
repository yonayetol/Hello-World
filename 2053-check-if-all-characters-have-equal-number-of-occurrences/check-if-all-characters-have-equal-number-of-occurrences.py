class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        new_s = Counter(s)
        to_be = new_s[s[0]]
        for char,count in new_s.items():
            if to_be != count:
                return False
        return True