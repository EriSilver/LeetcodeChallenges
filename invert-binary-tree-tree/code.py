class Solution(object):
    def recursion(self, tree):
        if tree:
            if (tree.right != None and type(tree.right) != type(4)):
                self.recursion(tree.right)
            if (tree.left != None and type(tree.left) != type(4)):
                self.recursion(tree.left)

            tmp = tree.left
            tree.left = tree.right
            tree.right = tmp
        
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.recursion(root)
        
        return root

"""
Runtime: 16 ms, faster than 84.35% of Python online submissions for Invert Binary Tree.
Memory Usage: 13.4 MB, less than 80.04% of Python online submissions for Invert Binary Tree.

All Time: 
Accepted: 851,501
Submissions: 1,218,159
"""