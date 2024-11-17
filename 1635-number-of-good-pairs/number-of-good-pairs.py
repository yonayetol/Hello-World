class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashmap = {}
        count = 0
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 0
            else:
                hashmap[i] += 1 

        for v in hashmap.values():
            if v != 0:
                count += (v+1)*v//2
        return count