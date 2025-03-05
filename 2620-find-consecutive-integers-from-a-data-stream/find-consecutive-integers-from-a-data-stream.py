class DataStream:

    def __init__(self, value: int, k: int):
        self.count = 0
        self.value = value
        self.k = k
        self.que = deque()

    def consec(self, num: int) -> bool:
        self.que.append(num)
        if num == self.value:
            self.count += 1

        if self.que and len(self.que) > self.k:
            tempo = self.que.popleft()
            if tempo == self.value:
                self.count -= 1

        return self.count == self.k

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)