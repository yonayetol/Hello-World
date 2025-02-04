class Solution:
    def removeComments(self, sources: List[str]) -> List[str]:
        answer = []
        opened = True
        i = j = 0
        small_str = ""
        while i < len(sources):
            while opened and i < len(sources) and j<len(sources[i]):
                if sources[i][j:j+2] == "/*":
                    opened = False
                    j += 2
                    break
                
                elif  sources[i][j:j+2] == "//": # ignoring everything when double slash occur
                    i += 1
                    j = 0
                    if small_str:
                        answer.append(small_str)
                    small_str = ""
                    continue

                small_str += sources[i][j]
                j += 1

                if j == len(sources[i]):
                    if small_str:
                        answer.append(small_str)
                    small_str = ""
                    i += 1
                    j = 0

            while not opened:
                if j >= len(sources[i]):
                    i += 1
                    j = 0
                    break

                if sources[i][j:j+2] == "*/":
                    opened = True                    
                    j += 1

                j += 1
                if j >= len(sources[i]):
                    i += 1
                    j = 0
                    if opened and small_str:
                        answer.append(small_str)
                        small_str = ""    
                
        return answer