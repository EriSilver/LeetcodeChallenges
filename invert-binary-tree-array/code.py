class Solution(object):
    def breakDesc(self, c, last):
        return c > last
    
    def breakAsc(self, c, last):
        return c <= last
    
    def whichDirection(self, root):
        if root[-1] > root[0] or root[-1] > root[-2]:
            return self.breakAsc
        else:
            return self.breakDesc
        
    def invertTree(self, root):
        """
        :type root: Array
        :rtype: Array
        """
        if len(root) < 3:
            return root
            
        self.boolFunction = self.whichDirection(root)
        newArray = []
        last = root[0]
        array = [last]
        
        for e in range(1, len(root)):
            
            if self.boolFunction(root[e], last):
                newArray.reverse()
                array += newArray
                newArray = []
                
            newArray += [root[e]]
            last = root[e]
        
        newArray.reverse()
        array += newArray
        
        return array