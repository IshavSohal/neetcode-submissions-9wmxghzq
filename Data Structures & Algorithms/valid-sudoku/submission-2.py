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
                print(' ')
                print('row')
                print(i)
                print('col')
                print(j)
                board_val = board[i][j] 
                if (board_val != "."):
                    num_val = int(board_val) - 1
                    # Update row hash
                    row_hash[i][num_val] += 1
                    if row_hash[i][num_val] > 1:
                        print('duplicate in row')
                        print('row')
                        print(i)
                        print('col')
                        print(j)
                        print('board val')
                        print(board_val)
                        return False
                    
                    # Update col hash
                    col_hash[j][num_val] += 1
                    if col_hash[j][num_val] > 1:
                        print('duplicate in col')
                        print('row')
                        print(i)
                        print('col')
                        print(j)
                        print('board val')
                        print(board_val)
                        return False

                    # Update square hash
                    print('squre index')
                    print((3 * i//3) + j//3)
                    square_hash[(3 * (i//3)) + j//3][num_val] += 1
                    if square_hash[i//3 + j//3][num_val] > 1:
                        print('duplicate in square')
                        print('row')
                        print(i)
                        print('col')
                        print(j)
                        print('board val')
                        print(board_val)
                        return False
        
        return True


        