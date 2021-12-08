# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def __init__(self):
        self.firstVal = None
        self.newHead = None
        
    def recursion(self, node):
        if node.next != None:
            nextNode = self.recursion(node.next)
        else:
            self.newHead = node
            return node
        
        nextNode.next = node
        if self.firstVal == node.val:
            node.next = None
        return node
    
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            self.firstVal = head.val
            self.recursion(head)
        return self.newHead

"""
    ALL TIME:
    Accepted: 1,773,834
    Submissions: 2,584,958

    Runtime: 62 ms, faster than 5.19% of Python online submissions for Reverse Linked List.
    Memory Usage: 18.6 MB, less than 17.25% of Python online submissions for Reverse Linked List.
"""