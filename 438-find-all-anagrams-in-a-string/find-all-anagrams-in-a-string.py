class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        right = len(p)
        final = []

        count_of_p = Counter(p)
        new_count = Counter(s[:len(p)])

        if new_count == count_of_p:
            final.append(0)

        for i in range(len(s)-len(p)):
            new_count[s[i]] -= 1
            new_count[s[right]] += 1
            if new_count[s[i]] == 0:
                del new_count[s[i]]
            if new_count == count_of_p:
                final.append(i+1)
            right += 1
        return final