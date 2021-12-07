# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def nodeToNum(node, digit=0, num=0):
    num += (node.val*(10**digit))
    if not node.next:
        return num
    return nodeToNum(node.next, digit+1, num)

def numToNode(num, node):
    n = num - num // 10 * 10
    node.val = n
    num //= 10
    if num == 0:
        return
    node.next = ListNode()
    return numToNode(num, node.next)
    
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node = ListNode()
        
        val1 = nodeToNum(l1)
        val2 = nodeToNum(l2)
        
        numToNode(val1 + val2, node)
        return node

'''
    ALL TIME:
    Accepted: 2,344,684
    Submissions: 6,279,788

    Runtime: 133 ms, faster than 5.12% of Python online submissions for Add Two Numbers.
    Memory Usage: 13.7 MB, less than 7.04% of Python online submissions for Add Two Numbers.
'''