class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        newS = ""
        maxLen = 0
        maxStr = ""
        newSFirstIndex = 0
        sLen = len(s)
        c = 0 
        
        while c < sLen:
            charIndex = s.rfind(s[c], newSFirstIndex, c)
            if charIndex > -1:
                newSLen = len(newS)
                if newSLen > maxLen:
                    maxLen = newSLen
                    maxStr = newS
                newS = ""
                c = charIndex + 1
                newSFirstIndex = c
            
            newS += s[c]
            c += 1
        
        newLen = len(newS)
        if newLen > maxLen: 
            return newLen
        return maxLen

'''
    ALL TIME:
    Accepted: 2,741,422
    Submissions: 8,429,528

    Runtime: 940 ms, faster than 13.73% of Python online submissions for Longest Substring Without Repeating Characters.
    Memory Usage: 13.8 MB, less than 51.07% of Python online submissions for Longest Substring Without Repeating Characters.
'''