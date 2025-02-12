class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        my_dict = {}
        for i in range(len(s)):
            my_dict[s[i]] = i
            
        left = 0
        i = 0
        answer = []
        while left < len(s) and i < len(s):
            left = my_dict[s[i]]
            j = i
            while j < left:
                left = max(left,my_dict[s[j]])
                j += 1
            answer.append(left+1-i)
            i = left+1

        return answer