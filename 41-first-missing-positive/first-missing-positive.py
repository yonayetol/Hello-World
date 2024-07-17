class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        should = 0
        hash_dict = {}
        for i in nums: 
            if i<=0:
                continue
            hash_dict[i] = should
            should +=1
#use of should ends here, let's reuse that variable
        if len(hash_dict) == 0 :
            return 1# ending is all nums are negatives
        should = max(nums) + 2
        for i in range(1,should):
            """we'll also check the last number+1,
which is the our last option if there is no missing positive"""
            if i not in hash_dict.keys():
                return i