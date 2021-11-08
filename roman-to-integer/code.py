class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        sLen = len(s)
        count = 0
        i = 0
        while i < sLen:
            num = d[s[i]]
            nextNum = 0
            if i + 1 < sLen:
                nextNum = d[s[i + 1]]
                
            if num < nextNum:
                count += (nextNum - num)
                i += 2
            else:
                count += num
                i += 1
                
        return count


"""
Runtime: 24 ms, faster than 98.95% of Python online submissions for Roman to Integer.
Memory Usage: 13.3 MB, less than 97.52% of Python online submissions for Roman to Integer.

All time:
Accepted: 1,219,059
Submissions: 2,114,087
"""