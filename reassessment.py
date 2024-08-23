#Enter the positions to be swapped
# define legal move
#check if initial board have legal move
#Use given positions to swap, check if index of cells in first row is same with 2nd row & 3rd row and index should not be more
#if same, means it's legal move, print message
#if not, print message 
#board is now 4X4, increase the index of row and column by 1, also increase check for index from 2 to 3
#it should work for both 3x3 & 4x4 boards
#add checks for l & t shapes

board = [
        [1, 2, 3, 4],
        [4, 4, 5, 4],
        [5, 3, 4, 6],
        [2, 2, 3, 5]
]
def spark_game(board, positions, direction):
    # Define legal move / same colored line
    board_size = len(board)

    def same_colored_line():
        for row in board:
            if len(set(row)) == 1:
                return True
        
        for col in range(board_size):
            first_item = board[0][col]
            all_col_items = True
            for row in range(1, board_size):
                if board[row][col] != first_item:
                    all_col_items = False
                    break
            if all_col_items:
                return True
                
        #check for L-shaped pattern
            
        #check for T-shaped pattern

        return False
        
    x, y = positions
    if direction == 'up':
        new_x, new_y = x - 1, y
    elif direction == 'down':
        new_x, new_y = x + 1, y
    elif direction == 'left':
        new_x, new_y = x, y - 1
    elif direction == 'right':
        new_x, new_y = x, y + 1
    else:
        print("Invalid direction")
        return 
        
    if not (0 <= new_x < board_size and 0 <= new_y < board_size):
        print("Choose position between 0 and (boardsize - 1)")
        return 

    board[x][y], board[new_x][new_y] = board[new_x][new_y], board[x][y]

    if same_colored_line():
        print("Board has a legal move")
    else:
        print("Board does not have a legal move")
    
    return board

spark_game(board, (1, 2), "up")

