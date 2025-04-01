class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def checker(maxSum):
            count = 1
            tempo = 0
            for num in nums:
                tempo += num
                if tempo > maxSum:
                    count += 1
                    tempo = num
            
            return count <= k

        mini = max(nums)
        maxi = sum(nums)
        while mini <= maxi:
            mid = (mini+maxi)//2
            if checker(mid): maxi = mid - 1
            else: mini = mid + 1

        return mini
