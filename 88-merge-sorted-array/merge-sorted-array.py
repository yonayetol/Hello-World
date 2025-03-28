class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        putter = m+n-1
        right1 = putter - n
        right2 = n - 1
        while right1 >= 0 and right2 >= 0: #nonnegative indexes
            if nums2[right2] >= nums1[right1]:
                nums1[putter] = nums2[right2]
                right2 -= 1
            else:
                nums1[putter] = nums1[right1]
                nums1[right1] = 0
                right1 -= 1
                
            putter -= 1
        # nums2 might left so finish that
        while right2>=0:
            nums1[putter] = nums2[right2]
            right2 -= 1
            putter -= 1
        