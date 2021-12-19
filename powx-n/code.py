class Solution(object):
    def smallN(self, n, div=0):
        if n < 1000:
            return n, div
        
        return self.smallN(n/10, div+10)
        
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        s = 1
        neg = n < 0
        
        if neg:
            n = -n
            
        newN, div = self.smallN(n)
        i = 0
        while i < newN:
            s *= x
            i += 1
            
        i = 0
        newS = s
        if div:
            while i < div + 1:
                newS *= s
                i += 1
            
        return 1/newS if neg else newS

'''
    Modified for big nums of n

    Failed here: 
    x = 1.00012
    n = 1024

    Output: 1.15820
    Expected: 1.13074
'''