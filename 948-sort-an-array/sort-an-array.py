class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def combine(arrA,arrB):
            answer = []
            left1 = left2 = 0
            while left1 < len(arrA) and left2 < len(arrB):
                if arrA[left1] < arrB[left2]: 
                    answer.append(arrA[left1])
                    left1 += 1
                else: 
                    answer.append(arrB[left2])
                    left2 += 1
            return answer+arrA[left1:]+arrB[left2:]

        def divide(left, right, nums):
            if left == right : return [nums[left]]
            mid = (left+right)//2
            return combine(divide(left, mid, nums), divide(mid+1, right, nums))
        return divide(0,len(nums)-1, nums)
