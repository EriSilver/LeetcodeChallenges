class Solution(object):
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
        i = 1
        while i <= n:
            s *= x
            i += 1
            
        return 1/s if neg else s

'''
    doesn't work when n is very big number

    Failed when 
    x = 0.00001
    n = 2147483647
'''