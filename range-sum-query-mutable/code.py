class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        
        self.sums = []
        
        i = 0
        self.numsLen = len(nums)
        self.divisible = 1500 if self.numsLen > 1500 else (self.numsLen // 1000  or self.numsLen // 500  or self.numsLen // 100  or self.numsLen // 10  or self.numsLen // 2 or 1)
        
        theInt = self.numsLen // self.divisible
        theFloat = self.numsLen / self.divisible
        
        for i in range((theInt + 1 if theFloat > theInt else theInt) + 1):
            start = i * self.divisible
            end = (i + 1) * self.divisible
            if end > self.numsLen:
                end = self.numsLen
            self.sums += [sum(nums[start  : end])]
            
    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        
        self.sums[index//self.divisible] += (val - self.nums[index])
        self.nums[index] = val
        

    #######################################################
    def extremity(self, left, right):
        
        # right excluded 
        if right - left > self.divisible / 2:
            count = 0
            partition = left // self.divisible
            numsIndex = partition * self.divisible
            # exclude the sum of the extremities 
            #right is wanted - left to be excluded 
            if numsIndex < left:
                count += (self.sums[partition] - sum(self.nums[numsIndex: left]))
            else: 
                #left is wanted - right to be excluded
                numsIndex += self.divisible
                if numsIndex > self.numsLen:
                      numsIndex = self.numsLen
                count += (self.sums[partition] - sum(self.nums[right: numsIndex]))
            return count
        else:
            return sum(self.nums[left:right])
    
    #######################################################
    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        count = 0
        isSamePartition = left // self.divisible == right // self.divisible
        # the left extremity |------#######|######
        # the right part is wanted and left to be excluded
        lastLeft = (self.divisible - (left % self.divisible)) + left
        count += self.extremity(left, lastLeft if not isSamePartition else right + 1)
        
        if not isSamePartition:
            # the right extremity #####|#######------|
            # the left part is wanted and right to be excluded
            firstRight = right - (right % self.divisible)
            count += self.extremity(firstRight if not isSamePartition else left, right + 1)  
            
            start = lastLeft // self.divisible
            end = firstRight // self.divisible 
            while start < end:
                count += self.sums[start]
                start += 1
                          
        return count
                        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

"""
Runtime: 1264 ms, faster than 98.20% of Python online submissions for Range Sum Query - Mutable.
Memory Usage: 32 MB, less than 83.78% of Python online submissions for Range Sum Query - Mutable.

____________________
*All Time:*     
Accepted: 166,230    
Submissions: 435,247
"""