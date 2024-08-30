class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        mini_list,choice = [0,1],2**(n-1)
        for i in range(2,n):
            right,turn = (k*2/choice>1),0
            if right:
                k -= 2**(n-i) #we need to diminish the index since we are going to leave, everything in the left
                turn = 1
            if mini_list[turn] == 1:# if we turn left turn is 0, so everything is fine
                mini_list = [1,0]
            else:
                mini_list = [0,1]
            choice /= 2 #always we are decreasing our choices by half
        return mini_list[k-1] # k is 1 or 2, so we'll decrease it by 1 and that is it!!
        
            