class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = {'u', 'r', 'e', 'i', 'o', 'q', 't', 'y', 'p', 'w'}
        row2 = {'k', 's', 'f', 'd', 'l', 'h', 'g', 'a', 'j'}
        row3 = {'x', 'z', 'c', 'n', 'm', 'b', 'v'}
        answer = []
        for word in words:
            char = word[0].lower()
            if char in row1:
                row_choice = row1
            elif char in row2:
                row_choice = row2
            else:
                row_choice = row3
            print(char,"is found in",row_choice)
            for i in range(len(word)):
                if word[i].lower() not in row_choice:
                    break
            else:
                answer.append(word)
        return answer