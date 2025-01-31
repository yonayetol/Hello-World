class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        other = []
        for i in range(len(nums)):
            # let's iterate over nums[i] by casting it into string
            for char in str(nums[i]):
                other.append(int(char)) # this will add the digits one by one
        return other