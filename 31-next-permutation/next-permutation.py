class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k,l = 0,len(nums)-1
        
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                k = i-1
        while l>k:
            if nums[l] > nums[k]:
                nums[k],nums[l] = nums[l],nums[k]
                break#2 3 1
            l -= 1
        else:
            k = -1
        l = len(nums)-1
        # k += 1
        print("nums = ",nums," and k,l ",k,l)
        for i in range(len(nums[k+1:])//2):
            nums[k+i+1],nums[l] = nums[l],nums[k+i+1]
            l -= 1
        
            