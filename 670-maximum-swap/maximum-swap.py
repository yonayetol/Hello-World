class Solution:
    def maximumSwap(self, num: int) -> int:
        num_list = list(map(int,str(num)))
        stack = []
        change = [n for n in range(len(num_list))] # [ 0 1 2 3 4 ]
        for i in range(len(num_list)):
            x = -1
            while len(stack)>=abs(x) and num_list[stack[x]]<=num_list[i]:
                change[stack[x]] = i        
                x -= 1
            stack.append(i) # 0 
        for i in range(len(num_list)):
            if i != change[i] and num_list[change[i]] != num_list[i]: #"if change is needed"
                num_list[i],num_list[change[i]] = num_list[change[i]],num_list[i]
                break
        x = "".join(str(s) for s in num_list)
        return int(x)