class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set1,ptr,length = set(),0,0
        for i in s:
            while i in set1: 
                set1.remove(s[ptr])
                ptr += 1     
            set1.add(i)
            length = max(length, len(set1))
        return length