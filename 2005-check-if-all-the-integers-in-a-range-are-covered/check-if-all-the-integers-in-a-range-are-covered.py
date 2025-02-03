class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        # let's create the set of numbers that we cover by the ranges
        my_set = {i for sub_list in ranges for i in range(sub_list[0],sub_list[1]+1)}

        answer = True
        while True and left <= right:
            if left not in my_set:
                answer = False
            left += 1
        return answer