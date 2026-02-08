# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        Answer = True
        def DFS(root):
            nonlocal Answer
            if not root: return -1
            
            hl = DFS(root.left)
            hr = DFS(root.right)
            Answer = Answer and (abs(hl-hr)) < 2
            return 1 + max(hl, hr)
        DFS(root)
        return Answer