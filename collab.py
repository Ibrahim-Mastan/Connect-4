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
        display_grid(grid)
        if game_won(grid):
            print("player 2 wins!")
            return

def player_V_random_bot():
    grid = create_grid(WIDTH,HEIGHT)
    display_grid(grid)
    player_to_move = 1
    while not game_drawn(grid):
        print("player 1 turn:   ")
        player_to_move = player_turn(player_to_move,grid)
        display_grid(grid)
        if game_won(grid):
            print("player 1 wins!")
            return
        print("Bot's Move :    ")
        player_to_move = random_bot_turn(player_to_move,grid)
        display_grid(grid)
        if game_won(grid):
            print("Bot wins!")
            return



def player_V_smart_bot():#need to code  this bot needs to try win and not lose rather than place randomly
    grid = create_grid(WIDTH,HEIGHT)
    display_grid(grid)
    player_to_move = 1
    while not game_drawn(grid):
        print("player 1 turn:   ")
        player_to_move = player_turn(player_to_move,grid)
        display_grid(grid)
        if game_won(grid):
            print("player 1 wins!")
            return
        print("Smart Bot's Move :   ")
        player_to_move = smart_bot_turn(grid,player_to_move)
        display_grid(grid)
        if game_won(grid):
            print("Smart Bot wins!")
            return



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

def smart_bot_turn(grid, player_to_move):
    # Check if bot can win by placing the piece
    for col in range(1,WIDTH+1):
        row = get_last_row(col, grid)
        if row != -1:
            #grid[col][row] = PLAYER_2_PIECE
            place_piece(col,grid,player_to_move)
            if game_won(grid):
                return swap_player(player_to_move)
            else:
                #grid[col][row] = BLANK_PIECE
                
                empty_piece(col,grid)
                

    # Pick a location for the bot to place the piece (same as random bot turn)
    valid = False
    count =  0
    while not valid and count < 30:
        col = input_random_location()
        row = get_last_row(col, grid)
        if row != -1:
            # Verify that if the bot places this piece the opponent cannot win on the next turn
            #grid[col][row] = PLAYER_2_PIECE
            place_piece(col,grid,player_to_move)
            if not can_opponent_win(grid,player_to_move):
                valid = True
                break
            else:
                #grid[col][row] = BLANK_PIECE
                empty_piece(col,grid)
        
        count += 1
    
    if count == 30:
        col = input_random_location()
        place_piece(col,grid,player_to_move)


    #place_piece(col, grid, player_to_move)
    return swap_player(player_to_move)

def can_opponent_win(grid,player_to_move):
    for col in range(1,WIDTH+1):
        row = get_last_row(col, grid)
        if row != -1:
            #grid[col][row] = PLAYER_1_PIECE
            place_piece(col,grid,swap_player(player_to_move))
            if game_won(grid):
                #grid[col][row] = BLANK_PIECE
                empty_piece(col,grid)
                return True
            else:
                #grid[col][row] = BLANK_PIECE
                empty_piece(col,grid)
    return False

    # x = input_location()
    # valid = False
    # while not valid:
    #     if validate_location_on_grid(x,grid):
    #         if not column_full(x,grid):
    #             valid = True
    #             break
    #         x = input_location()

    
    
    """
    first go through every position and check if bot can win by placing the piece. if so place the piece and win, other move on.

    then pick a location for the bot to place the piece (same as random bot turn)
    then we need to verify that if the bot places this piece the opponent cannot win on the next turn
    if not, we place the piece
    else pick another position and check again(loop this until we find a position that does work or no more positions left)
    then we are done
    dont use chat gpt for this as it will just confuse you. 
    """

def place_piece(x,grid,player):
    row = get_last_row(x,grid)
    if player == 1:
        piece = PLAYER_1_PIECE
    else:
        piece = PLAYER_2_PIECE
    grid[row][x-1] = piece

def empty_piece(x,grid):
    row = get_last_row(x,grid) + 1
    
    grid[row][x-1] = BLANK_PIECE



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
