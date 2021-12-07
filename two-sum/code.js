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
    let xx = 0;
    let yy = 0;
    let arrxy = [];
    let xLength = x.length;
    let yLength = y.length;

    for ( let e = 0, n = xLength + yLength; e < n; e++){
        let thex = xx < xLength? x[xx]: x[xLength-1];
        let they = yy < yLength?y[yy]: y[yLength-1];

        if (thex > theTarget && they > theTarget){
            return arrxy;
        }

        if (thex < they && thex <= theTarget){
            if (xx < xLength){
                arrxy = arrxy.concat(thex);
                xx += 1;
            }
            else{
                arrxy = arrxy.concat(they);
                yy += 1;
            }
        }
        else if (thex > they && they <= theTarget){
            if (yy < yLength){
                arrxy = arrxy.concat(they);
                yy += 1;
            }
            else{
                arrxy = arrxy.concat(thex);
                xx += 1;
            }
        }
        else if (thex <= theTarget){
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

/*********************************/
var theTarget = 0;
var twoSum = function(nums, target) {
    if (nums.toString().includes("-"))
        theTarget = 100000000;
    else
        theTarget = target;
    // original indeces before sort
    let oldnums = [...nums];
    nums = ssort(nums);
    for(let i in nums){
        let newArray = nums.slice(parseInt(i)+1);
        let remainder = target - nums[i];
        let otherIndex = binarySearch(newArray, remainder, parseInt(i) + 1);

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