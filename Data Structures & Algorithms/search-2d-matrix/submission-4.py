class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row = 0
        row_max = len(matrix) - 1

        while row <= row_max:
            low = 0
            high = len(matrix[0]) - 1
            while low <= high:

                mid = low + (high - low) // 2

                if matrix[row][mid] == target:
                    return True
                
                elif matrix[row][mid] < target:
                    low = mid + 1

                else: 
                    high = mid - 1
            row += 1

        return False