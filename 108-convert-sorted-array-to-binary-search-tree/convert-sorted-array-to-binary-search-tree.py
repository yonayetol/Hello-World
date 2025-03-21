# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def recurseThis(start,end):
            mid = max((start+end) // 2, 0)
            curr = TreeNode(nums[mid])

            if start > end: return None
            if start == end: return curr
            
            curr.left = recurseThis(start, mid-1)
            curr.right = recurseThis(mid+1, end)

            return curr

        return recurseThis(0,len(nums)-1)