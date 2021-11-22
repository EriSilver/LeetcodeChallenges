/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

 var twoSum = function(nums, target) {
    for(let i in nums){
        i = parseInt(i);
        let remainder = target - nums[i];
        let otherIndex = nums.indexOf(remainder, i + 1);

        if (otherIndex !== -1){
            return [i, otherIndex];
        }
    }
};