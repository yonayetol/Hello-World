from heapq import heapify, heappop, heappush
from math import sqrt
from typing import List

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-gift for gift in gifts]
        heapify(gifts)

        for _ in range(k):
            heappush(gifts, -int(sqrt(-heappop(gifts))))

        return -sum(gifts)