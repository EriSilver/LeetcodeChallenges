class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.nums[index] = val
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        count = 0
        while left <= right:
            count += self.nums[left]
            left += 1
        return count
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)