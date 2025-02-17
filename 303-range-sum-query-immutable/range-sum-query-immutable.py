class NumArray:
    def __init__(self, nums: List[int]):
        self.my_array = []
        adder = 0
        for i in range(len(nums)):
            self.my_array.append(nums[i] + adder)
            adder += nums[i]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.my_array[right]
        return self.my_array[right] - self.my_array[left-1]