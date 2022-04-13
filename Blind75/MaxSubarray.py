def maxSubArray(nums):
    maxSum = nums[0]
    currSum = 0
    for num in nums:
        currSum = max(currSum + num, num)
        print(currSum)
        maxSum = max(currSum,maxSum)
        
    return maxSum
    
            