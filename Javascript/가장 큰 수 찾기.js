let nums = [10,55,234,678,45,67,32,56,78,98]
let max = nums[0]

for(let i = 0; i < nums.length; i++) {
    if(max < nums[i]) {
        max = nums[i]
    }
}

console.log("최대값:"+max)