class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def possible(gap):
            basket = 1
            past = position[0]
            for num in position[1:]:
                if num-past >= gap:
                    past = num
                    basket += 1
            return basket>=m

        left = 0
        right = position[-1]-position[0]

        while left <= right:
            middle = (left + right)//2
            if possible(middle):
                left = middle + 1
            else:
                right = middle - 1
        return right
