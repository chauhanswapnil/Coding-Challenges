from typing import (
    List,
)

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[List[int]]) -> bool:
        # Write your code here
        intervals.sort()
        prevEnd = intervals[0][1]
        for start,end in intervals[1:]:
            if start < prevEnd:
                return False
            prevEnd = end
        return True
print(Solution().can_attend_meetings([[5,8],[9,15]]))