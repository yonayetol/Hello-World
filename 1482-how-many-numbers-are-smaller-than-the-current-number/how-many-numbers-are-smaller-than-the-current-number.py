class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        the_copy = sorted(nums[:])
#         1 2 2 3 8
        final =[]
        for i in nums:
            location = the_copy.index(i)# the place of i in the_copy
            final.append(location)
        return final