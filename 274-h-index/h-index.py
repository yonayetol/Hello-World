class Solution:
    def hIndex(self, citations: List[int]) -> int:
        my_counter = [0]*1001
        for i in citations:
            my_counter[i] += 1

        the_more = 0
        answer = 0
        for i in range(1000,-1,-1):
            the_more += my_counter[i]
            if the_more >= i:
                return i