# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        sum = 0
        def dfs(binary_string, node):
            nonlocal sum
            if node == None: return
            binary_string += str(node.val)
            dfs(binary_string, node.left)
            dfs(binary_string, node.right)
            if node.left == None and node.right == None:
                sum += int(binary_string, 2)
        dfs("", root)
        return sum
        