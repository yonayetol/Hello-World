class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        a = (num-3)/3
        if a != int(a):
            return []
        a = int(a)
        return [a,a+1,a+2]