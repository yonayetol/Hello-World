class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        my_dict,ptr = {},0
        for i in range(len(numbers)):
            if numbers[i] in my_dict:
                return [my_dict[numbers[i]]+1,i+1]
            my_dict[target-numbers[i]] = i
            