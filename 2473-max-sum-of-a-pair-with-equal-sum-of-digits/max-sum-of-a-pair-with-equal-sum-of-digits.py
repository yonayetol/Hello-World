class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def digit_sum(num):
            sums=0
            while num:
                sums+=(num%10)
                num//=10
            return sums
        my_sorting = [0]*82
        answer = -1
        for i in range(len(nums)):
            little_sum = digit_sum(nums[i])
            if my_sorting[little_sum] == 0:
                my_sorting[little_sum] = [nums[i]]
            else:
                my_sorting[little_sum].append(nums[i])
                my_sorting[little_sum].sort()# sorting of 2 or 3 numbers always
                my_sorting[little_sum] = my_sorting[little_sum][-2:]
                answer = max(answer,my_sorting[little_sum][0]+my_sorting[little_sum][1])
        return answer