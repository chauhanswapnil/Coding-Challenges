def binarySearch(nums, target):
    left = 0
    right = len(nums) - 1
    while(left<=right):
        mid = (left+right) // 2
        if target < nums[mid]:
            right = mid - 1
        if target > nums[mid]:
            left = mid + 1
        if target == nums[mid]:
            return mid
    return -1

print(binarySearch([0,1,2,3,4,5,6], 7))