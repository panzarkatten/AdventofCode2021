from pathlib import Path

input = Path(__file__).with_name('day11_test.txt')
raw_input = input.open('r').read()

def process_input(input):
    """Process the input and return an object which is easier to work with"""
    data = list([list(map(int, line)) for line in list(input.strip().split('\n'))])
    
    return data

def get_adj_pos(pos, grid):
    # Setup
    x,y = pos
    grid_size = get_grid_size(grid)
    x_lim = grid_size['x'] - 1
    y_lim = grid_size['y'] - 1

    # Calculate new positions
    neighbours_pos = [
        (x     , y - 1), # N
        (x + 1 , y - 1), # NE
        (x + 1 , y    ), # E
        (x - 1 , y + 1), # SE
        (x     , y + 1), # S
        (x - 1 , y + 1), # SW
        (x - 1 , y    ), # W
        (x - 1 , y - 1)  # NW
    ]

    # Check if any of the positions is out of bound
    for i,v in enumerate(neighbours_pos):
        xn,yn = v
        if any([xn < 0, xn > x_lim, yn < 0, yn > y_lim]):
           neighbours_pos[i] = False 

    return neighbours_pos

def get_pos_data(pos, grid):
    x,y = pos
    return grid[y][x]

def set_pos_data(pos, data, grid):
    x,y = pos
    grid[y][x] = data
    return grid

def get_grid_size(grid):
    return {'x': len(grid[0]) - 1, 'y': len(grid) - 1}

def grid_increase(grid, num):
    grid_size = get_grid_size(grid)
    x_lim = grid_size['x']
    y_lim = grid_size['y']
    
    for y in range(y_lim):
        for x in range(x_lim):
            grid[y][x] += num
    
    return grid

# --- Init ---
grid = process_input(raw_input)
print(input)
# --- Part One ---
for i in range(2):
    # Increase all positions with one
    grid = grid_increase(grid, 1)


for r in grid:
    for c in r:
        print(c, end='\t')
    
    print('')

# --- Part Two ---
