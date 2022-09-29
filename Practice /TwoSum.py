
def twoSum(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        comp = target - nums[i]
        if comp in hashmap:
            return [i, hashmap[comp]]
        hashmap[nums[i]] = i
    print(hashmap)

print(twoSum([2,7,11,15],9))
