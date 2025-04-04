class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arrSum = 0
        for i in range(n):
            num = abs(nums[i])
            arrSum += num
            if nums[num-1] > 0: #we didn't accessed it before
                nums[num-1] *= -1
            else:
                duplicate = num
        
        return [duplicate, (pow(n,2)+n)//2 - arrSum + duplicate]