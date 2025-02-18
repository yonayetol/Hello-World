class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        my_dict = Counter({0: 1})
        running,count = 0,0
        for i in range(len(nums)):
            running += nums[i]
            if running - k in my_dict:
                count += my_dict[running - k]
            my_dict[running] += 1
        return count
        