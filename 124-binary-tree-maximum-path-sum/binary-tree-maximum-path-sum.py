# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.total = float('-inf')
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if not root: return 0

            lMax = helper(root.left)
            rMax = helper(root.right)

            tempo = root.val + max(lMax,0) + max(0, rMax)
            self.total = max(self.total, tempo )

            return max(root.val, root.val + max(lMax, rMax))

        helper(root)
        return self.total
