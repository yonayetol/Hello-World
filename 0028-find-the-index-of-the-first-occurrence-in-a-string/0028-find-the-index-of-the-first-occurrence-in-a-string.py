class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        else:
            my_list=list(haystack)
            wanted=list(needle)
            indexes=[]
            for n in range(len(haystack)):
                pre=n
                for m in range(len(needle)):
                    if haystack[pre]==needle[m]:
                        indexes.append(pre)
                        if len(indexes)==len(needle):
                            return indexes[0]
                    else:
                        indexes=[]
                        break
                    pre+=1
            return -1