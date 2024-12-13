class Solution:
    def findScore(self, nums: List[int]) -> int:
        sorted_index = sorted(range(len(nums)), key = lambda i: nums[i])
        my_dict = {}
        answer = 0
        for i in sorted_index:
            if i not in my_dict:
                my_dict[i] = None
                if i != 0 and i != len(nums)-1:
                    my_dict[i+1] = None
                    my_dict[i-1] = None
                elif i==0:    
                    my_dict[i+1] = None
                else:
                    my_dict[i-1] = None      
                answer += nums[i]    
        return answer