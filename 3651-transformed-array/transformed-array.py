class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        other = [0]*len(nums)
        for i in range(len(nums)):
            tempo = i + nums[i]
            if nums[i] >= 0:# meaning we move forward
                other[i] = nums[tempo%(len(nums))]
            else:# for back ward moves
                if abs(tempo) <= len(nums):
                    other[i] = nums[tempo]
                else:
                    other[i] = nums[-1*(abs(tempo)%len(nums))]
        return other        

#3 -6 1 1
#   1-6 = -5
# abs(-5) = 5 is > len() which is 4 so 5%4 times -1
#