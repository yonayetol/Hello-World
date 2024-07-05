class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_2=nums[:]# I copied the list so as not to affect the original list
        Output=[]#this will constitute our answer
        for n in nums:
            nums_2.remove(n)
            reduced=len(nums)-len(nums_2)
            for n_2 in nums_2:
                if n+n_2==target:
                    Output.append(nums.index(n))
                    Output.append(nums_2.index(n_2)+reduced)
                    break
        return Output[:2]