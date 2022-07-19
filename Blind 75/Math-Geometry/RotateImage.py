from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1
        while l<r:
            for i in range(r-l):
                top, bottom = l,r
                # Saving the top left
                topLeft = matrix[top][l + i]
                # Bottom left to top left
                matrix[top][l+i] = matrix[bottom-i][l]
                # Bottom right to bottom left
                matrix[bottom-i][l] = matrix[bottom][r-i]
                # Top right to bottom right
                matrix[bottom][r-i] = matrix[top+i][r]
                # Top left to top right
                matrix[top+i][r] = topLeft
            r-=1
            l+=1