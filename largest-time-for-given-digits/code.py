class Solution(object):
    def stringFormat(self, num):
        if num >= 10:
            return str(num)
        else:
            return "0" + str(num)
        
    def iteration(self, array, ignore):
        first = -1
        second = -1
        array.sort(reverse=True)
        for e in array:
            if e <= 2 and e not in ignore:
                first = e
                array.remove(e)
                break
        
        if first == -1:
            return None, None
        
        for e in array:
            if (first * 10 + e) <= 23:
                second = e
                array.remove(e)
                break
                
        return first, second
        
    def largestTimeFromDigits(self, arr):
        """
        :type arr: List[int]
        :rtype: str
        """
        try:
            array = arr[:]
            ignore = []

            first, second = self.iteration(array, ignore)
            if first == None and second == None:
                return ""
            for i in range(4):
                if first == None and second == None:
                    return ""
                if len(array) > 2 or (array[0] > 5 and array[1] > 5):
                    array += [first, second]
                    ignore += [first]
                    first, second = self.iteration(array, ignore)
                else:
                    break

            third = ""

            if array[0] <= 5:
                third += (str(array[0]) + str(array[1]))
            else:
                third += (str(array[1]) + str(array[0]))


            return self.stringFormat(first*10 + second) + ":" + third

        except:
            return ""


##########################################################################################

#evaluation
'''
Runtime: 16 ms, faster than 94.92% of Python online submissions for Largest Time for Given Digits.
Memory Usage: 13.5 MB, less than 49.15% of Python online submissions for Largest Time for Given Digits.

###########################################################################################
The challenge's all people accepted and submissions counts:
Accepted: 66,530
Submissions: 185,960
https://leetcode.com/problems/largest-time-for-given-digits/submissions/
'''