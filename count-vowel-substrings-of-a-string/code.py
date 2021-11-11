class Solution(object):
    def countVowelSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        vowels = ["a","e","i","o","u"]
        
        vowelsCopy = vowels[:]
        count = 0
        repeats = 1
        lastIndex = -1
    
        for n in range(len(word)):
            e = word[n]
            if e in vowels:
                if e in vowelsCopy:
                    vowelsCopy.remove(e)
                    if lastIndex == -1:
                        lastIndex = n

                    if not vowelsCopy:
                        count += repeats

                else:
                    while word[lastIndex] in word[lastIndex + 1 : n + 1]:
                        repeats += 1
                        lastIndex += 1

                    if not vowelsCopy:
                        count += repeats
                        
            else:
                vowelsCopy = vowels[:]
                repeats = 1
                lastIndex = -1
                
        return count


"""
Runtime: 16 ms, faster than 96.86% of Python online submissions for Count Vowel Substrings of a String.
Memory Usage: 13.4 MB, less than 89.24% of Python online submissions for Count Vowel Substrings of a String.

All Time: 
Accepted: 9,063
Submissions: 13,691
"""