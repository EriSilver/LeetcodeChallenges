class Solution(object):
    limit = 2**31
    upperLimit = limit - 1
    lowerLimit = limit * -1
    
    def finalNum(self, num, negative):
        if self.lowerLimit <= num <= self.upperLimit:
            if negative:
                return -num
            return num
        return 0
    
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = x < 0
        num = x
        newNum = 0
        
        if negative:
            num = -num
            
        while num > 0:
            newNum = newNum * 10 + (num % 10)
            num //= 10
            
        return self.finalNum(newNum, negative)

"""
    ALL TIME:
    Accepted: 1,861,767
    Submissions: 7,089,756

    Runtime: 40 ms, faster than 7.04% of Python online submissions for Reverse Integer.
    Memory Usage: 13.3 MB, less than 67.76% of Python online submissions for Reverse Integer.
"""