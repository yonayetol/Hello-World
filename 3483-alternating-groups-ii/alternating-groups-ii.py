class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        left, right, count, n = 0, 1, 0, len(colors)

        while right < n + k - 1:
            if colors[right % n] + colors[(right-1) % n] != 1:
                left = right
            right += 1
            if right - left == k:
                count += 1
                left += 1
                
        return count