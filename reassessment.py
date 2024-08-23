#Enter the positions to be swapped
# define legal move
#check if initial board have legal move
#Use given positions to swap, check if index of cells in first row is same with 2nd row & 3rd row and index should not be more
#if same, means it's legal move, print message
#if not, print message 

def spark_game(positions, direction):
    board = [
        [1, 2, 3],
        [4, 4, 5],
        [5, 3, 4]
    ]
    # define legal move / same colored line
    def same_colored_line():
        for row in board:
            if row[0] == row[1] == row[2]:
                print("True")
                return True
            for col in range(3):
                #print(">>",board[2][col])
                if board[0][col] == board[1][col] == board[2][col]:
                    print("True")
                    return True
        print("False")
        return False
    
    legal_move = same_colored_line()
    
    if legal_move == False:
        print("Initial board does not have legal move")
    
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
        
    if not (0 <= new_x < 3 and 0 <= new_y < 3):
        print("Choose position btw 0 & 2")
        return False

    board[x][y], board[new_x][new_y] = board[new_x][new_y], board[x][y]
    if legal_move == True:
        print("Board has a legal move")
    else:
        print("Board does not have a legal move")
    return legal_move

spark_game((5,2), "up")
    


