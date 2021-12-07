class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        newS = ""
        maxLen = 0
        maxStr = ""
        sLen = len(s)
        c = 0 
        
        while c < sLen:
            if s[c] in newS:
                newSLen = len(newS)
                if newSLen > maxLen:
                    maxLen = newSLen
                    maxStr = newS
                newS = ""
                c = s.rindex(s[c], 0, c) + 1
            
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

    Runtime: 947 ms, faster than 13.71% of Python online submissions for Longest Substring Without Repeating Characters.
    Memory Usage: 13.6 MB, less than 88.44% of Python online submissions for Longest Substring Without Repeating Characters.
'''