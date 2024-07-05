class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def my_love(given):
            num=len(min(given,key=len))
            output=""
            letters=[]
            for m in range(num):
                for n in range(len(given)-1):
                    if given[n][m]!=given[n+1][m]:
                        return output
                output+=given[n][m]
            return(output)
        if len(strs)>1:
            final=my_love(strs)
            return final
        else:
            return strs[0]