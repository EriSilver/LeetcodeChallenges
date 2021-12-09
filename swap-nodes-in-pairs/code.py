# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        one = head
        prev = None
        if one and one.next:
            head = one.next
            while one and one.next:
                two = one.next
                three = two.next

                tmp = one
                one.next = two.next
                two.next = tmp

                if prev:
                    prev.next = two

                if one.next:
                    prev = one
                    one = one.next

        return head

"""
ATT TIME:
Accepted: 727,972
Submissions: 1,293,441

Runtime: 16 ms, faster than 84.91% of Python online submissions for Swap Nodes in Pairs.
Memory Usage: 13.4 MB, less than 85.95% of Python online submissions for Swap Nodes in Pairs.
"""