from pathlib import Path

input = Path(__file__).with_name('day9.txt')
raw_input = input.open('r').read()

def process_input(input):
    """Process the input and return an object which is easier to work with"""
    data = list([list(map(int, line)) for line in list(input.strip().split('\n'))])
    
    return data

def get_pos_height(pos, map):
    x,y = pos
    return map[y][x]

def get_neighbours_height(neighbours, map):
    neighbour_heights = []
    for p in neighbours:
        if p:
            neighbour_heights.append(get_pos_height(p, map))
        else:
            neighbour_heights.append(False)
    
    return neighbour_heights

def get_neighbour_pos(pos, map):
    # Setup
    x,y = pos
    map_size = get_map_size(map)
    map_x_lim = map_size['x'] - 1
    map_y_lim = map_size['y'] - 1

    # Calculate new positions
    neighbours_pos = [
        (x     , y - 1),
        (x + 1 , y    ),
        (x     , y + 1),
        (x - 1 , y    )
    ]

    # Check if any of the positions is out of bound
    for i,v in enumerate(neighbours_pos):
        xn,yn = v
        if any([xn < 0, xn > map_x_lim, yn < 0, yn > map_y_lim]):
           neighbours_pos[i] = False 

    return neighbours_pos


def get_map_size(map):
    return {'x': len(map[0]), 'y': len(map)}


def get_low_spots(map):
    low_spots = []
    map_size = get_map_size(map)
    for y in range(0, map_size['y']):
        for x in range(0, map_size['x']):
            nb_positions = get_neighbour_pos((x,y), map)
            nb_heights = get_neighbours_height(nb_positions, map)
            pos_h = get_pos_height((x,y), map)

            if pos_h < min(nb_heights):
                low_spots.append((x,y))
    
    return low_spots


def get_basin(pos, map):
    basin = []
    if pos:    
        pos_height = get_pos_height(pos, map)
        nb_positions = get_neighbour_pos(pos, map)
        nb_heights = get_neighbours_height(nb_positions, map)

        found_basin = False
        new_basin = []
        for i,v in enumerate(nb_heights):
            if v > pos_height and nb_positions[i] and v != 9:
                found_basin = True
                new_basin.append(nb_positions[i])

        if found_basin:
            for p in new_basin:
                if p not in basin:
                    basin += get_basin(p, map)
        
        basin.append(pos)
        basin = list(set(basin))

        return basin
            


# --- Init ---
flow_map = process_input(raw_input)
low_spots = get_low_spots(flow_map)

# --- Part One ---
sum = 0
for p in low_spots:
    sum += get_pos_height(p, flow_map) + 1

print(f'Part One: {sum}')

# --- Part Two ---
basins = [get_basin(ls, flow_map) for ls in low_spots]
top3 = list(sorted(basins, key = len, reverse = True))[:3]
l = list(map(len,top3))
prod = l[0] * l[1] * l[2]

print(f'Part Two: {prod}')