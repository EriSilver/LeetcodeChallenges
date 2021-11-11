class Solution(object):
    def countVowelSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        vowels = ["a","e","i","o","u"]
        
        vowelsCopy = vowels[:]
        count = 0
        i = -1
        repeats = 1
        lastIndex = -1
    
        for n in range(len(word)):
            e = word[n]
            if e in vowels:
                if e in vowelsCopy:
                    vowelsCopy.remove(e)
                    if i == -1:
                        i = n
                        lastIndex = i

                    if not vowelsCopy:
                        count += repeats

                else:
                    if e == word[lastIndex]: # palindrome
                        repeats += 1
                        lastIndex += 1

                    if not vowelsCopy:
                        count += repeats
            else:
                i = -1
                vowelsCopy = vowels[:]
                repeats = 1
                lastIndex = -1
            print("____", count, repeats, lastIndex)
                        
        return count