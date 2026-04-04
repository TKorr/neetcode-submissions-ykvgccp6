class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix[0]) - 1
        row = 0
        row_max = len(matrix) - 1

        while row <= row_max:
            l, h = low, high
            while l <= h:

                mid = l + (h - l) // 2

                if matrix[row][mid] == target:
                    return True
                
                elif matrix[row][mid] < target:
                    l = mid + 1

                else: 
                    h = mid - 1
            row += 1

        return False