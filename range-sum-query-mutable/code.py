class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        
        self.sums = []
        
        i = 0
        self.numsLen = len(nums)
        theInt = self.numsLen // 20
        theFloat = self.numsLen / 20
        
        for i in range((theInt + 1 if theFloat > theInt else theInt) + 1):
            start = i * 20
            end = (i + 1) * 20
            if end > self.numsLen:
                end = self.numsLen
            self.sums += [sum(nums[start  : end])]
            
    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        
        self.sums[index//20] += (val - self.nums[index])
        self.nums[index] = val
        

    #######################################################
    def extremity(self, left, right):
        
        # right excluded 
        if right - left > 10:
            count = 0
            partition = left // 20
            numsIndex = partition * 20
            # exclude the sum of the extremities 
            #right is wanted - left to be excluded 
            if numsIndex < left:
                count += (self.sums[partition] - sum(self.nums[numsIndex: left]))
            else: 
                #left is wanted - right to be excluded
                numsIndex += 20
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
        isSamePartition = left // 20 == right // 20
        # the left extremity |------#######|######
        # the right part is wanted and left to be excluded
        lastLeft = (20 - (left % 20)) + left
        count += self.extremity(left, lastLeft if not isSamePartition else right + 1)
        
        if not isSamePartition:
            # the right extremity #####|#######------|
            # the left part is wanted and right to be excluded
            firstRight = right - (right % 20)
            count += self.extremity(firstRight if not isSamePartition else left, right + 1)  
            
            start = lastLeft // 20
            end = firstRight // 20 
            while start < end:
                count += self.sums[start]
                start += 1
                          
        return count
                        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)