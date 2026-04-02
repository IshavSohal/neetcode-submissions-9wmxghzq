class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        low_row = 0
        high_row = m - 1

        while low_row <= high_row:
            mid_row = (high_row + low_row) // 2
            curr_row = matrix[mid_row]

            # Perform binary search on the middle row
            low = 0
            high = n - 1
            while low <= high:
                mid = (high + low) // 2
                if curr_row[mid] == target:
                    return True
                elif curr_row[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            # If the target was not in this middle row, we update the row indices accordingly
            if curr_row[0] > target:
                high_row = mid_row - 1
            else:
                low_row = mid_row + 1

        return False
