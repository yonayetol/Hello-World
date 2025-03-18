# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(root, minim, maxim, answer):
            if not root: return answer
            if root.val > maxim: maxim = root.val
            if root.val < minim: minim = root.val
            
            return max(helper(root.left, minim, maxim, max(answer, maxim-minim)),helper(root.right, minim, maxim, max(answer, maxim-minim)))

        return helper(root, root.val, root.val, 0)
