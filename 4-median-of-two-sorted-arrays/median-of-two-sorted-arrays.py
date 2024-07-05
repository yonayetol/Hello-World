class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        dotet=nums1+nums2
        dotet.sort()
        if len(dotet)%2!=0:
            ind=len(dotet)//2
            return ( dotet[ind])
        else:
            x=len(dotet)//2
            return ((dotet[x-1]+dotet[x])/2)