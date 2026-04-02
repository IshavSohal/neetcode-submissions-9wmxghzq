class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash = []
        for i in range(9):
            row_hash.append([0]*9)
        
        col_hash = []
        for i in range(9):
            col_hash.append([0]*9)

        square_hash = []
        for i in range(9):
            square_hash.append([0]*9)

        for i in range(9):
            for j in range(9):
                board_val = board[i][j] 
                if (board_val != "."):
                    num_val = int(board_val) - 1
                    # Update row hash
                    row_hash[i][num_val] += 1
                    if row_hash[i][num_val] > 1:
                        return False
                    
                    # Update col hash
                    col_hash[j][num_val] += 1
                    if col_hash[j][num_val] > 1:
                        return False

                    # Update square hash
                    square_index = (3 * (i//3)) + j//3
                    square_hash[square_index][num_val] += 1
                    if square_hash[square_index][num_val] > 1:
                        return False
        
        return True


        