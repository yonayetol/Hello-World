class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        the_big = int(c**0.5)+1
        reminder = set()
        for i in range(the_big):
            pro = pow(i,2)
            reminder.add(pro)
            if c-pro in reminder:
                return True
                break
        return False