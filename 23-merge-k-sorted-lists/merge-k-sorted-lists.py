# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        realAnswer = ListNode()
        answer = realAnswer

        n = len(lists)
        ThereAreLeft = True
        while ThereAreLeft:
            TheminNode = -1
            theMinNum = float('inf')    
            ThereAreLeft = False
            for i in range(n):
                # iterate over all linkedlist and 
                # save where the minimum is and delete that node from that linkedlist.
                currLL = lists[i]
                if currLL:
                    currVal = currLL.val
                    ThereAreLeft = True
                    if currVal < theMinNum:
                        theMinNum = currVal
                        TheminNode = i
                # print(theMinNum,"from:- ", TheminNode ,"curr index = ", i)
                
            if TheminNode != -1:
                answer.next = ListNode(theMinNum)
                answer = answer.next
                if lists[TheminNode]: lists[TheminNode] = lists[TheminNode].next
                else: lists[TheminNode] = None
        
        return realAnswer.next


