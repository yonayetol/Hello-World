class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evens_sum = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                evens_sum += nums[i]

        answer = []
        for num,ind in queries:
            if nums[ind] % 2 == 0:
                evens_sum -= nums[ind]
            nums[ind] += num
            if nums[ind] % 2 == 0:
                evens_sum += nums[ind]
            answer.append(evens_sum)

        return answer