class Solution(object):
    def largestTimeFromDigits(self, arr):
        """
        :type arr: List[int]
        :rtype: str
        """
        template = [2,3,5,9]
        done = [None, None, None, None]
        array = arr[:]
        for e in arr + array:
            for o in range(4):
                b = e <= template[o] if o != 1 else (e <= 9 and e >= 0 and (done[0] or 0) + (done[1] or 0) < 24)
                if e in array and e >= (done[o] or 0) and b and e >= 0:
                    tmp = done[o]
                    done[o] = e
                    array.remove(e)
                    if tmp != None:
                        array += [tmp]            
            
        string = ""    
        for i in done:
            if i == None:
                return ""
            string += str(i)
         
        return string[:2] + ":" + string[2:]