class Solution:
    def minimumSteps(self, s: str) -> int:
        left = 0
        right = len(s)-1
        swap_count = 0
        
        while left < right:
            if int(s[left]) + int(s[right]) == 1:
                if s[left] == '1' and s[right] == '0':
                    swap_count += right - left
                left += 1
                right -= 1 
            elif s[left] == '1' and s[right] == '1':
                right -= 1
            else:
                left += 1

        return swap_count