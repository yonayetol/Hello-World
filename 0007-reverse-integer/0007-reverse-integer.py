class Solution:
    def reverse(self, x: int) -> int:
        new_x=str(x)[::-1]
        try:
            if new_x[-1]=="-":
                new_x=new_x[:-1]
            final=int(new_x)
            if final > 2147483647:
                final=0
            if x<0:
                final*=-1
        except:
            pass
        return final