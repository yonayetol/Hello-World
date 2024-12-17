class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        other = [0]*(max(nums)+1)
        for i in range(len(nums)):
            print("now:",i)
            other[nums[i]] += 1
        new_dict,place = {},0
        for i in range(len(other)):
            if other[i]>0:
                new_dict[i] = place
                place += other[i]
                
        for i in range(len(nums)):
            nums[i] = new_dict[nums[i]]
        return nums

       
