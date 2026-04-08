class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # identify correct row
        # n - row
        # m - col
        target_row = 0



        for n, col in enumerate(matrix):
            last_row_val = col[len(col)-1]
            # print(n, col, last_row_val)
            if target <= last_row_val:
                target_row = n
                break


        # print(target_row)
        # print(matrix[target_row])

        if target in matrix[target_row]:
            return True
        return False


        # use b-search on row
