class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        my_dict = [[] for _ in range(101)]
        for i in range(len(nums)):
            my_dict[nums[i]].append(i)
        runing = 0
        for i in range(len(my_dict)):
            if my_dict[i]:
                for j in range(len(my_dict[i])):
                    for m in range(j+1,len(my_dict[i])):
                        if my_dict[i][j]*my_dict[i][m] % k == 0:
                            runing += 1
                            print(my_dict[i][j],my_dict[i][m])
        return runing