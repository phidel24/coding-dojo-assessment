#Enter the positions to be swapped
# define legal move
#check if initial board have legal move
#Use given positions to swap, check if index of cells in first row is same with 2nd row & 3rd row and index should not be more
#if same, means it's legal move, print message
#if not, print message 
#board is now 4X4, increase the index of row and column by 1, also increase check for index from 2 to 3

board = [
        [1, 2, 3, 4],
        [4, 4, 5, 4],
        [5, 3, 4, 6],
        [2, 2, 3, 5]
]
def spark_game(board, positions, direction):
    # Define legal move / same colored line
    def same_colored_line():
        for row in board:
            if row[0] == row[1] == row[2] == row[3]:
                return True
        
        for col in range(4):
            if board[0][col] == board[1][col] == board[2][col] == board[3][col]:
                return True

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
        
    if not (0 <= new_x < 4 and 0 <= new_y < 4):
        print("Choose position between 0 and 3")
        return 

    board[x][y], board[new_x][new_y] = board[new_x][new_y], board[x][y]

    if same_colored_line():
        print("Board has a legal move")
    else:
        print("Board does not have a legal move")
    
    return board

spark_game(board, (2, 2), "up")

