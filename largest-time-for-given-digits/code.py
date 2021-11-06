class Solution(object):
    def largestTimeFromDigits(self, arr):
        """
        :type arr: List[int]
        :rtype: str
        """
        array = arr[:]
        array.sort(reverse=True)
        
        first = -1
        for e in array:
            if e <= 2:
                first = e * 10
                array.remove(e)
                break
        
        if first == -1:
            return ""
        
        for e in array:
            if first + e <= 23:
                first += e
                array.remove(e)
                break
                
        if len(array) > 2:
            return ""
        
        second = ""
        
        if array[0] <= 5:
            second += (str(array[0]) + str(array[1]))
        else:
            if array[1] > 5:
                return ""
            second += (str(array[1]) + str(array[0]))
            
        return (str(first) if first > 9 else "0" + str(first)) + ":" + second