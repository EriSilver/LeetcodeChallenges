# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def __init__(self):
        self.n = None
        self.node = None
        
    def recursion(self, node):
        if node.next:
            count = self.recursion(node.next)
        else:
            count = 1
        
        if count:
            if count == self.n:
                self.node = node.next
            if count == self.n + 1:
                node.next = self.node
                return None
            return count + 1
        
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        self.n = n
        
        if self.recursion(head) == n + 1:
            return self.node

        return head

"""
    ALL TIME:
    Accepted: 1,128,927
    Submissions: 3,024,850

    Runtime: 20 ms, faster than 74.07% of Python online submissions for Remove Nth Node From End of List.
    Memory Usage: 13.5 MB, less than 45.33% of Python online submissions for Remove Nth Node From End of List.
"""