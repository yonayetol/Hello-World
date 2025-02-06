class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        my_dict,count = {},0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                prod = nums[i]*nums[j]
                if prod not in my_dict:
                    my_dict[prod] = 0
                my_dict[prod] += 1

        for prod,c in my_dict.items():
            count += c*(c-1)//2
        return count*8