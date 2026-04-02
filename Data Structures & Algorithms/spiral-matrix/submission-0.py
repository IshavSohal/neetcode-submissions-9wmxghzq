class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        if m <= n:
            numIterations = 2*m - 1
        else:
            numIterations = 2*n
        res = []

        # We iterate over a total of m distinct rows and n distinct columns
        for x in range(numIterations):

            # If this is an even numbered iteration, we are processing a row
            if x % 2 == 0:
                # Determine which row is being processed, which direction we are processing
                # from, and the start/end indices
                if x % 4 == 0:
                    row = x // 4
                    start = max(0, (x // 4) - 1)
                    end = n-1 - (x // 4)
                    if x < numIterations-1:
                        end -= 1
                    for i in range(start, end+1):
                        res.append(matrix[row][i])
                else:
                    row = m-1 - (x - 2) // 4
                    start = n-1 - (x // 4)
                    end = x // 4
                    if x < numIterations-1:
                        end += 1
                    for i in range(start, end-1, -1):
                        res.append(matrix[row][i])   

            # If this is an odd numbered iteration, we are processing a column
            else:
                if ((x - 1) % 4) == 0:
                    col = n-1 - (x - 1)//4
                    start = (x - 1)//4
                    end = m-1 - (x - 1)//4
                    if x < numIterations-1:
                        end -= 1
                    for i in range(start, end+1):
                        res.append(matrix[i][col])
                else:
                    col = (x - 1)//4
                    start = m-1 - (x - 1)//4
                    end = ((x - 1)//4) + 1
                    if x < numIterations-1:
                        end += 1
                    for i in range(start, end-1,-1):
                        res.append(matrix[i][col])

        return res
                 


            