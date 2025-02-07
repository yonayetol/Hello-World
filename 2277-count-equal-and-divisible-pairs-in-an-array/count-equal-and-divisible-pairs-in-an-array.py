class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        my_dict = dict()
        for i in range(len(nums)):
            if nums[i] not in my_dict:
                my_dict[nums[i]] = []
            my_dict[nums[i]].append(i)
        runing = 0
        for e,l_i in my_dict.items():
            for i in range(len(l_i)):
                for j in range(i+1,len(l_i)):
                    if my_dict[e][i]*my_dict[e][j] % k == 0:
                        runing += 1

        return runing