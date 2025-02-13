class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, i, my_dict, the_max = -1,0,{},0

        while i < len(s):
            while i < len(s) and (s[i] not in my_dict or my_dict[s[i]]<left):
                my_dict[s[i]] = i
                i += 1
                the_max = max(the_max, i-(left+1))
                if i == len(s):
                    return max(the_max, i-(left+1))

            left = my_dict[s[i]] # have a mercy for letters before left
            the_max,my_dict[s[i]] = max(the_max, i-left), i
            i += 1
        return the_max


