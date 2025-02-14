class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        the_sum = float('inf')
        tempo = 0
        for i in range(len(nums)-1):
            left = i + 1
            right = len(nums)-1
            while left < right:
                tempo = nums[i] + nums[left] + nums[right]
                if abs(tempo-target) < abs(the_sum-target):
                    the_sum = tempo
                if tempo > target:
                    right -= 1
                else:
                    left += 1
                
            if tempo == target:
                break
        return the_sum