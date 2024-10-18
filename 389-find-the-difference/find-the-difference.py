class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        my_dict = Counter(s)
        for char in t:
            if char not in my_dict:
                return char
            else:
                my_dict[char] -= 1
                if my_dict[char] == 0:
                    del my_dict[char]