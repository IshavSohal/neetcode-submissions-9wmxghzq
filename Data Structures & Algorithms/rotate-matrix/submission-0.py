class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # Step 1: flip each column
        for col in range(n):
            for row in range(n//2):
                opp_row = n - row - 1
                temp = matrix[row][col]
                matrix[row][col] = matrix[opp_row][col]
                matrix[opp_row][col] = temp


        # Step 2: flip across top-left to bottom-right diagonal
        for col in range(n):
            for row in range(col+1, n):
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp

        