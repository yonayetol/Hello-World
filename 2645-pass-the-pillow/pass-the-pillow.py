class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        going_up = True
        now = 1
        for i in range(time):
            if going_up:
                now += 1
                if now == n:
                    going_up = False
            else:
                now -= 1
                if now == 1:
                    going_up = True
        return now