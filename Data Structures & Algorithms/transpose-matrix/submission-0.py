class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        res = []

        for col in range(n):
            curr_row = []

            for row in range(m):
                curr_row.append(matrix[row][col])
            
            res.append(curr_row)

        return res