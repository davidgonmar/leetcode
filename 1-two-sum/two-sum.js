/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {

    for(let index1 in nums){
        for(let index2 in nums){
                if (index1==index2) continue;
                if (nums[index1] + nums[index2] === target) return [index1, index2];
        }
    }
} ;    
