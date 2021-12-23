class Solution(object):
    def smallN(self, n, div=0, x=0):
        if not x:
            x = 10
            while (n % x) > 0 and x > 1:
                x -= 1
            
        if n < 1000 or x == 1 or (x and (n % x) > 0):
            return n, div 

        return self.smallN(n/x , div + x, x)
        
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if (-0.001 <= x <= 0.001) and not(-2 <= n <= 2):
            return 0
            
        s = 1
        neg = n < 0
        
        if neg:
            n = -n
            
        newN, div = self.smallN(n)
        i = 0
        while i < newN:
            s *= x
            i += 1
        
        newS = s
        if div:
            i = 1
            while i < div:
                newS *= s
                i += 1
            
        return 1/newS if neg else newS

'''
    Modified for big nums of n

    the problem is adding 2 divs (second recursion in smallN)

    Failed here: 
    x = 1.00001
    n = 123456

    Output: 1.15820
    Expected: 1.13074
'''

"""
test examples:
1.00001
123456

1.00012
20502
1.00012
1024
2.00000
10
0.00001
2147483647
2.10000
3
2.00000
-2
0.44528
0
0.05930
2
"""