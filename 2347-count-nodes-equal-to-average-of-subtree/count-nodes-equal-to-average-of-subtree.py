class Solution:
    def __init__(self):
        self.matchingSubtreeCount = 0
    def calculateSubtreeValues(self, currentNode):
        if currentNode is None:
            return 0, 0  
            
        leftSubtree  = self.calculateSubtreeValues(currentNode.left)
        rightSubtree = self.calculateSubtreeValues(currentNode.right)

        # Calculate the sum of values and the number of nodes in the current subtree.
        sumOfValues  = leftSubtree [0] + rightSubtree[0] + currentNode.val
        numberOfNodes  = leftSubtree [1] + rightSubtree[1] + 1

        # Check if the current node's value matches the average of its subtree.
        if sumOfValues  // numberOfNodes  == currentNode.val:
            self.matchingSubtreeCount += 1

        return sumOfValues , numberOfNodes   # Return the calculated values for the current subtree.


    def averageOfSubtree(self, root):
        self.calculateSubtreeValues(root)  # Start the DFS from the root node.
        return self.matchingSubtreeCount 