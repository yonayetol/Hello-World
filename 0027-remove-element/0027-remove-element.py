class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        for n in range(len(nums)):
            if nums[i]==val:
                nums.pop(i)
                i-=1
            i+=1
        return len(nums)