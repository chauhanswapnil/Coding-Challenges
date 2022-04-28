from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        a,b = newInterval
        start = -1
        end = -1
        arr = []
        for interval in intervals:
            s, e = interval
            if (b > e):
                arr.append(interval)
            if a >= s and a<=e:
                start = s
            elif start != -1 and end == -1 and e < b:
                if s > b:
                    end = b
                if s < b:
                    end = e
                arr.append([start,end])
                # arr.append(interval)
            # else:
            #     arr.append(interval)
        return arr

o = Solution()

print(o.insert([[1,3],[6,9]] , [2,5]))

print(o.insert([[1,2],[3,5],[6,7],[8,10],[12,16]] , [4,8]))