"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self): self.answer = []
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return
        self.answer.append(root.val)
        for NODE in root.children:
            self.preorder(NODE)
        
        return self.answer