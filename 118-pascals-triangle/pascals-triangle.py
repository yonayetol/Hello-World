class Solution:
    def __init__(self):
        self.total = [[1]]
    def generate(self, numRows: int) -> List[List[int]]:

        def helper(x):
            if x == 0:
                return [1]

            prev = helper(x-1)
            for i in range(len(prev)-1):
                prev[i] += prev[i+1]

            prev = [1] + prev

            self.total.append(prev)

            return prev[:]

        helper(numRows-1)
        return self.total