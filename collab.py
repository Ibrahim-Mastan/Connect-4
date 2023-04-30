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
def validate_location_on_grid(x):
    return  x > 0 and x <= WIDTH
def player_turn(player,grid): 
    x = input_location()
    valid = False
    while not valid:
        if validate_location_on_grid(x):
            if not column_full(x,grid):
                valid = True
                break
        print("Error try again")
        x = input_location()
    
    place_piece(x,grid,player)

def place_piece(x,grid,player): #This isn't complete
    grid[5][x-1] = PLAYER_1_PIECE


def game_ended(grid):#This is not complete
    return False

main()