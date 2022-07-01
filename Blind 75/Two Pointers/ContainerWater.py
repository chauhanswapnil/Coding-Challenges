class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        L = 0
        R = len(height) - 1
        
        while L < R:
            area = min(height[L], height[R]) * (R-L)
            if area > maxarea:
                maxarea = area
            if height[L] > height[R]:
                R-=1
            else:
                L+-1
        
        return maxarea