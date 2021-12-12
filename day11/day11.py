from pathlib import Path

input = Path(__file__).with_name('day11.txt')
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
        (x + 1 , y + 1), # SE
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
    return {'x': len(grid[0]), 'y': len(grid)}

def pos_increase(pos, num, grid):
    x,y = pos
    grid[y][x] += num
    return grid

def grid_increase(grid, num):
    grid_size = get_grid_size(grid)
    x_lim = grid_size['x']
    y_lim = grid_size['y']
    
    for y in range(y_lim):
        for x in range(x_lim):
            grid[y][x] += num
    
    return grid

def flash_octopi(grid):
    grid_size = get_grid_size(grid)
    x_lim = grid_size['x']
    y_lim = grid_size['y']
    counter = 0
    triggered = []
    stop = False
    all_flashed = False

    while stop == False:
        trig = False
        num_flashed = 0
        for x in range(x_lim):
            for y in range(y_lim):
                d = get_pos_data((x,y), grid)
                if d >= 10:
                    counter += 1
                    num_flashed += 1
                    trig = True
                    grid = set_pos_data((x,y), 0, grid)
                    triggered.append((x,y))
                    adj = get_adj_pos((x,y), grid)
                    for p in adj:
                        if p and p not in triggered:
                            xa, ya = p
                            grid = pos_increase((xa,ya), 1, grid)

        if trig == False:
            stop = True
    
    return grid, counter        

# --- Init ---
grid = process_input(raw_input)
flashed_octopi = 0
step_all_flashed = None
print(input)
# --- Part One ---
for i in range(100):
    # Increase all positions with one
    grid = grid_increase(grid, 1)
    grid, flashed = flash_octopi(grid)
    flashed_octopi += flashed

print(f'Part One: {flashed_octopi}')


# --- Part Two ---
grid = process_input(raw_input)
step = 1

while step_all_flashed == None:
    # Increase all positions with one
    grid = grid_increase(grid, 1)
    grid, flashed = flash_octopi(grid)
    # print(f'Flashed octopi at step {step}: {flashed}')
    if flashed == 100:
        step_all_flashed = step
    step += 1

print(f'Part Two: {step_all_flashed}')