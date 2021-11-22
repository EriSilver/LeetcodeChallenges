/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

/*****************************/
// Merge sort
function ssort(arr){ 
    const arrLength = arr.length;
    if (arrLength <= 1)
        return arr
    else{
        let left = ssort(arr.slice(0, parseInt(arrLength/2)));
        let right = ssort(arr.slice(parseInt(arrLength/2)));
        return merge(left, right);
    }
}

function merge(x,y){
    let xx = 0
    let yy = 0
    let arrxy = []

    for ( let e in [...x, ...y]){
        let xLength = x.length;
        let thex = xx < xLength? x[xx]: x[xLength-1];
        let yLength = y.length;
        let they = yy < yLength?y[yy]: y[yLength-1];

        if (thex < they){
            if (xx < xLength){
                arrxy = arrxy.concat(thex);
                xx += 1;
            }
            else{
                arrxy = arrxy.concat(they);
                yy += 1;
            }
        }
        else if (thex > they){
            if (yy < yLength){
                arrxy = arrxy.concat(they);
                yy += 1;
            }
            else{
                arrxy = arrxy.concat(thex);
                xx += 1;
            }
        }
        else{
            if( xx < xLength){
                arrxy = arrxy.concat(thex);
                xx += 1;
            }
            if (yy < yLength){
                arrxy = arrxy.concat(they);
                yy += 1;
            }
        }
    }
    return arrxy;
}
/***************************/
// recursion - binary search
// returns index of the remainder
function binarySearch(array, remainder, startingIndex){
    let arrayLength = array.length;
    if (arrayLength === 1){
        if (array[0] === remainder)
            return startingIndex;
        else
            return;
    }
    else if (arrayLength === 0)
        return;
    else {
        let halfLength = parseInt(arrayLength / 2);
        if (array[halfLength] === remainder)
            return startingIndex + halfLength;
        else if (remainder < array[halfLength]){
            return binarySearch(array.slice(0, halfLength), remainder, startingIndex);
        }
        else {
            return binarySearch(array.slice(halfLength + 1), remainder, startingIndex + halfLength + 1);
        }
    }
}


var xx = [];
function largerThanTarget(array, remainder, startingIndex){
    let arrayLength = array.length;
    if (arrayLength === 1){
        if (array[0] === remainder)
            return startingIndex;
        else if (array[0] > remainder){
            xx = xx.slice(0, startingIndex);
            return;
        }
        else
            return;
    }
    else if (arrayLength === 0)
        return;
    else {
        let halfLength = parseInt(arrayLength / 2);
        if (array[halfLength] === remainder)
            return startingIndex + halfLength;
        else if (remainder < array[halfLength]) {
            xx = xx.slice(0, startingIndex + halfLength);
            return binarySearch(array.slice(0, halfLength), remainder, startingIndex);
        }
    }
}


/*********************************/
var theTarget = 0;
var twoSum = function(nums, target) {
    theTarget = target;
    // original indeces before sort
    let oldnums = [...nums];
    nums = ssort(nums);
    xx = [...nums];
    let toSliceHere = largerThanTarget(nums, target - nums[0], 0);
    if (toSliceHere){
        if (nums[0] === nums[toSliceHere]){
            return [oldnums.indexOf(nums[0]), oldnums.lastIndexOf(nums[0])];
        }
        else {
            return [oldnums.indexOf(nums[0]), oldnums.indexOf(nums[toSliceHere])];
        }
    }

    nums = xx;
    for(let i in nums){
        i = parseInt(i);
        let newArray = nums.slice(i+1);
        let remainder = target - nums[i];
        let otherIndex = binarySearch(newArray, remainder, i + 1);

        if (otherIndex){
            if (nums[i] === nums[otherIndex]){
                return [oldnums.indexOf(nums[i]), oldnums.lastIndexOf(nums[i])];
            }
            else {
                return [oldnums.indexOf(nums[i]), oldnums.indexOf(nums[otherIndex])];
            }
        }
    }
};