class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        my_dict_S = [1]*(len(nums))

        for i in range(n-2,-1,-1):
            my_dict_S[i] = my_dict_S[i+1] * nums[i+1]
            
        running = 1
        for i in range(n):
            my_dict_S[i] *= running
            running *= nums[i]
        return my_dict_S