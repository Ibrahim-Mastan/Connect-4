import random

WIDTH = 7
HEIGHT = 6
PLAYER_1_PIECE = "X"
PLAYER_2_PIECE = "O"
BLANK_PIECE = " "
def create_grid(rows, cols):
    grid = []
    for _ in range(cols):
        column = [BLANK_PIECE] * rows
        grid.append(column)
    return grid

def display_grid(grid):
    print("  " + '   '.join(map(str, range(1, len(grid[0]) + 1))))
    for row in grid:
        print('│ ' + ' │ '.join(row) + ' │')
        print('────' * len(row) + '│')

def menu():
    print(""" 
    1. player v player
    2. player v random bot
    3. player v smart bot

    chooose an option(1-3): 
    """)
    choice = input("")
    return choice

def is_choice_valid(choice):
    try:
        choice = int(choice)
    except:
        return False
    if choice < 1:
        return False
    elif choice > 3:
        return False
    else:
        return True

def main():

    choice = menu()
    while not is_choice_valid(choice):
        choice = menu()
    choice = int(choice)
    if choice == 1:
        player_V_Player()
    elif choice == 2:
        player_V_random_bot()
    elif choice == 3:
        player_V_smart_bot()

def player_V_Player():
    grid = create_grid(WIDTH, HEIGHT)
    display_grid(grid)
    player_to_move = 1
    while not game_drawn(grid):
        print("player 1 turn: ")
        player_to_move = player_turn(player_to_move,grid)
        display_grid(grid)
        if game_won(grid):
            print("player 1 wins!")
            return
        print("player 2's turn: ")
        player_to_move = player_turn(player_to_move,grid)

def player_V_random_bot():
   for row in board:
        print('|'.join(row))
print('---------------')

def is_valid_move(board, col):
    return board[0][col] == ' '

def make_move(board, col, player):
    for row in range(5, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = player
            break

def is_winner(board, player):
    # Check rows
    for row in range(6):
        for col in range(4):
            if board[row][col] == player and board[row][col+1] == player and \
                    board[row][col+2] == player and board[row][col+3] == player:
                return True
    # Check columns
    for col in range(7):
        for row in range(3):
            if board[row][col] == player and board[row+1][col] == player and \
                    board[row+2][col] == player and board[row+3][col] == player:
                return True
    # Check diagonal (top-left to bottom-right)
    for row in range(3):
        for col in range(4):
            if board[row][col] == player and board[row+1][col+1] == player and \
                    board[row+2][col+2] == player and board[row+3][col+3] == player:
                return True
    # Check diagonal (bottom-left to top-right)
    for row in range(3, 6):
        for col in range(4):
            if board[row][col] == player and board[row-1][col+1] == player and \
                    board[row-2][col+2] == player and board[row-3][col+3] == player:
                return True
    return False

def random_bot_move(board):
    valid_moves = [col for col in range(7) if is_valid_move(board, col)]
    if valid_moves:
        return random.choice(valid_moves)
    else:
        return None

def player_V_random_bot():
    board = [[' ' for _ in range(7)] for _ in range(6)]
    player = 'X'
    
    while True:
        display_grid(board)
        
        if player == 'X':
            col = int(input("Enter your move (column number): "))  # Human player's move
        else:
            col = random_bot_move(board)  # Random bot's move

        if col is None:
            print("It's a draw!")
            break
        
        if is_valid_move(board, col):
            make_move(board, col, player)
            if is_winner(board, player):
                display_grid(board)
                print(f"Player {player} wins!")
                break
            player = 'O' if player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")

player_V_random_bot()


"""
 grid = create_grid(WIDTH,HEIGHT)
    player_to_move = 1
    while not game_ended(grid):
        display_grid(grid)
        print("player 1 turn:   ")
        player_to_move = random_bot_turn(random_bot_turn,grid)
        display_grid(grid)
        print("Bot's Move :    ")
        random_to_move = random_bot_turn(random_to_move,grid)
 """

def player_V_smart_bot():
    pass
def input_location():  #returns a location from the user or return -1 if error
    x = input("Enter Location: ")
    
    try:
        x = int(x)
    except:
        x = -1
    return x

def input_random_location():
    x = random.randint(1,WIDTH)
    return x

def column_full(x,grid):
    return False
def validate_location_on_grid(x,grid):
    return  x > 0 and x <= WIDTH and get_last_row(x,grid) != -1
def player_turn(player,grid): 
    x = input_location()
    valid = False
    while not valid:
        if validate_location_on_grid(x,grid):
            if not column_full(x,grid):
                valid = True
                break
        print("Error try again")
        x = input_location()
    
    place_piece(x,grid,player)
    return swap_player(player)

def random_bot_turn(player,grid):
    x = input_random_location()
    valid = False
    while not valid:
        if validate_location_on_grid(x,grid):
            if not column_full(x,grid):
                valid = True
                break
        x = input_random_location()
    
    place_piece(x,grid,player)
    return swap_player(player)

def smart_bot_turn(grid):
    pass

def place_piece(x,grid,player):
    row = get_last_row(x,grid)
    if player == 1:
        piece = PLAYER_1_PIECE
    else:
        piece = PLAYER_2_PIECE
    grid[row][x-1] = piece

def swap_player(player):
    return player*-1

def get_last_row(column,grid): 
# get the last available row in the column or return -1 if full
    row = HEIGHT-1
    piece = grid[row][column-1]
    while piece != BLANK_PIECE and row > 0:
        row -= 1
        piece = grid[row][column-1]
    
    if piece == BLANK_PIECE:

        return row
    return -1

def game_won(grid):
    # Check rows for a win
    for row in grid:
        for col in range(WIDTH - 3):
            if row[col] != BLANK_PIECE and row[col] == row[col + 1] == row[col + 2] == row[col + 3]:
                print ("You won!, ggez!")
                return True

    # Check columns for a win
    for col in range(WIDTH):
        for row in range(HEIGHT - 3):
            if grid[row][col] != BLANK_PIECE and grid[row][col] == grid[row + 1][col] == grid[row + 2][col] == grid[row + 3][col]:
                return True

    # Check diagonals (top-left to bottom-right) for a win
    for col in range(WIDTH - 3):
        for row in range(HEIGHT - 3):
            if grid[row][col] != BLANK_PIECE and grid[row][col] == grid[row + 1][col + 1] == grid[row + 2][col + 2] == grid[row + 3][col + 3]:
                return True

    # Check diagonals (top-right to bottom-left) for a win
    for col in range(WIDTH - 3):
        for row in range(3, HEIGHT):
            if grid[row][col] != BLANK_PIECE and grid[row][col] == grid[row - 1][col + 1] == grid[row - 2][col + 2] == grid[row - 3][col + 3]:
                return True

    return False
def game_drawn(grid):
    if game_won(grid):
        return False
    for col in grid:
        for piece in col:
            if piece == BLANK_PIECE:
                return False
    return True


main()
menu()
