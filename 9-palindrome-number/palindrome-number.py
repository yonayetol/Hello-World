class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return (None)
        new_s=str(x)
        my_list=[m for m in new_s]
        my_sum=0
        for n in range(len(my_list)):
            if my_list[n]==my_list[-n-1]:
                my_sum+=1
        if my_sum==len(my_list):
            return "true"
        else:
            return