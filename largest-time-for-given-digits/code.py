class Solution(object):
    def stringFormat(self, num):
        if num >= 10:
            return str(num)
        else:
            return "0" + str(num)
        
    def largestTimeFromDigits(self, arr):
        """
        :type arr: List[int]
        :rtype: str
        """
        array = arr[:]
        array.sort(reverse=True)
        print(array)
        
        for e in range(4):
            first = array[e] * 10 + array[(e + 1) % 4]
            second = array[(e + 2) % 4] * 10 + array[(e + 3) % 4]
            
            print(first, second)
            if first > 23 and second > 59:
                return ""
            elif first <= 23 and second <= 59:
                return self.stringFormat(first) + ":" + self.stringFormat(second)
            else:
                if e == 3:
                    first = array[e] * 10 + array[(e + 1) % 4]
                    second = array[(e + 3) % 4] * 10 + array[(e + 2) % 4]
                    print(first, second)
                    if first <= 23 and second <= 59:
                        return self.stringFormat(first) + ":" + self.stringFormat(second)
        
        return ""