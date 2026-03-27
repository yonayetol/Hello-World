class Solution:
    def isPossible(self, target):
        heap = [-num for num in target]
        heapify(heap)
        curr = sum(target)
        while True:
            top = -heappop(heap)
            rest = curr - top

            if top == 1 or rest == 1: return True
            if rest == 0 or top <= rest: return False

            new_val = top % rest
            if new_val == 0: return False

            heappush(heap, -new_val)
            curr = rest + new_val