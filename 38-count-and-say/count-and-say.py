class Solution:
    def countAndSay(self, n: int) -> str:
        new = "1"
        for i in range(1,n):
            ptr = 0
            left = 0
            new_new = ""
            while ptr < len(new):
                left = ptr
                ptr += 1
                while ptr < len(new) and new[ptr] == new[left]:
                    ptr += 1
                new_new += f"{ptr-left}{new[left]}"
                
            new = new_new

        return new