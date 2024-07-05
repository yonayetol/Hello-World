class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """add each characters to a list one after the other while doing so 
check if the first character is repeated(by looping) if so terminate the loop by break"""
        # let's change my string to a list
        my_list=list(s)
        the_copy=my_list[:]
        new_str=""
        my_only=[]
        for lt in my_list:
            location=the_copy.index(lt)
            the_copy[location]="\u2764"
            for char in my_list[location:]:
                if char not in new_str:
                    new_str+=char
                else:
                    my_only.append(new_str)
                    new_str=""
                    break
        # now my_only possess all substrings without repeating characters
        # so let's check the longest and return the length of the characters
        lens=0
        for lengths in my_only:
            if len(lengths)>lens:
                lens=len(lengths)
        if len(s)==1:
            lens=1
        
        return lens