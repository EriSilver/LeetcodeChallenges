class Solution(object):
    def merge(self, n, m):
        newArray = []
        tn = 0
        tm = 0
        nlength = len(n)
        mlength = len(m)
        if nlength == 0:
            return m, mlength
        elif mlength == 0:
            return n, nlength
        
        while tn < nlength and tm < mlength:
            if n[tn] < m[tm]:
                newArray += [n[tn]]
                tn += 1
            else:
                newArray += [m[tm]]
                tm += 1
                
            if tn == nlength:
                newArray += m[tm:]
                break
            if tm == mlength:
                newArray += n[tn:]
                break
                
        return newArray, nlength + mlength
            
        
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        newArray, arrLength = self.merge(nums1, nums2)
        
        if arrLength % 2 == 0:
            l = arrLength // 2
            return (newArray[l] + newArray[l-1]) / 2.0
        else:
            return newArray[arrLength // 2]

"""
    ALL TIME:
    Accepted: 1,172,224
    Submissions: 3,530,830

    Runtime: 76 ms, faster than 66.97% of Python online submissions for Median of Two Sorted Arrays.
    Memory Usage: 13.6 MB, less than 54.67% of Python online submissions for Median of Two Sorted Arrays.
"""