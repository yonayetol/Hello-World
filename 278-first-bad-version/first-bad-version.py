class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        mid = (left+n)//2
        while left < n:
            if not isBadVersion(mid-1) and isBadVersion(mid): return mid
            if isBadVersion(mid):
                n = mid - 1
            else:
                left = mid + 1
            mid = (left+n)//2

        return max(left, n)
