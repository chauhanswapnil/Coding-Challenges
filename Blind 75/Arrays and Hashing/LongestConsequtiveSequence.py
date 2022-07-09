class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        curr = 0
        currLongest = 0
        setNums = set(nums)
        for val in setNums:
            if (val-1) not in setNums:
                curr+=1
                nextNum = val+1
                while (nextNum in setNums):
                    if nextNum in setNums: curr+=1
                    nextNum+=1
                if curr > currLongest: currLongest = curr
                curr = 0
        return currLongest