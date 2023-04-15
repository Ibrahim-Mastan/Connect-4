def create_grid(rows, cols):
    grid = []
    for _ in range(rows):
        row = [' '] * cols
        grid.append(row)
    return grid

def display_grid(grid):
    print("  " + '   '.join(map(str, range(1, len(grid[0]) + 1))))
    for row in grid:
        print('│ ' + ' │ '.join(row) + ' │')
        print('────' * len(row) + '│')

rows = 6
cols = 7
grid = create_grid(rows, cols)
display_grid(grid)
