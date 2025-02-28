class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.ptr = 0
        
    def visit(self, url: str) -> None:
        i = len(self.stack) - 1
        while i > self.ptr:
            self.stack.pop()
            i -= 1
        self.stack.append(url)
        self.ptr += 1

    def back(self, steps: int) -> str:
        self.ptr = max(self.ptr - steps,0)
        return self.stack[self.ptr]

    def forward(self, steps: int) -> str:
        self.ptr = min(self.ptr + steps, len(self.stack)-1)
        return self.stack[self.ptr]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)