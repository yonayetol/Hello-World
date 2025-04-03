class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        premax, postmax = [], []
        preMaxi, postMaxi = float('-inf'), float('-inf')
        for i in range(len(nums)):
            premax.append(preMaxi)
            postmax.append(postMaxi)
            preMaxi, postMaxi = max(preMaxi, nums[i]), max(postMaxi, nums[len(nums)-1-i])

        postmax = postmax[::-1]
        answer = float('-inf')
        for i in range(len(nums)-1): 
            answer = max(answer, (premax[i]-nums[i])*postmax[i])

        return max(answer, 0)