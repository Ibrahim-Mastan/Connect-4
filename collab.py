WIDTH = 9
HEIGHT = 7
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
def main():

    grid = create_grid(WIDTH, HEIGHT)
    player_to_move = 1
    while not game_ended(grid):
        display_grid(grid)
        print("player 1 turn: ")
        player_to_move = player_turn(player_to_move,grid)
        display_grid(grid)
        print("player 2's turn: ")
        player_to_move = player_turn(player_to_move,grid)
def input_location():  #returns a location from the user or return -1 if error
    x = input("Enter Location: ")
    
    try:
        x = int(x)
    except:
        x = -1
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

def game_ended(grid):#This is not complete
    return False

main()