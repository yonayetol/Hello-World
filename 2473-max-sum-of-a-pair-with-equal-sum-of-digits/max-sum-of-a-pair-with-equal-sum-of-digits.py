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
                heapify(my_sorting[little_sum])
            else:
                heappush(my_sorting[little_sum],nums[i])
                if len(my_sorting[little_sum]) > 2:
                    heappop(my_sorting[little_sum])
                answer = max(answer,my_sorting[little_sum][0]+my_sorting[little_sum][1])

        return answer