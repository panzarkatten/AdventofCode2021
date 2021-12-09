from pathlib import Path
from typing import Tuple, List, Dict

input = Path(__file__).with_name('day9.txt')
raw_input = input.open('r').read()

def process_input(input: str) -> List[Tuple[Tuple[str, str]]]:
    """Process the input and return an object which is easier to work with"""

    data = list([list(map(int, line)) for line in list(input.strip().split('\n'))])
    
    return data

def get_pos_height(pos: Tuple[int, int], map: List[List[int]]):
    x,y = pos
    return map[y][x]

def get_neighbour_pos(pos):
    x,y = pos

    u = (x     , y - 1)
    r = (x + 1 , y    )
    d = (x     , y + 1)
    l = (x - 1 , y    )
    
    return {'u': u,'r': r,'d': d,'l': l}

print(f'Neighbour positions: {get_neighbour_pos((4,4))}')

def get_neighbours(pos: Tuple[int, int], map: List[List[int]]) -> List[int]:
    """
    Returned list contains neighbour in the order UP, RIGHT, DOWN, LEFT
    If nieghbour is out of bound the max height if 9 is used instead
    """
    n = []
    
    # Position to check
    x,y = pos
    y = int(y)
    x = int(x)

    # Map limits
    map_size = get_map_size(map)
    map_x_lim = len(map[0]) - 1
    map_y_lim = len(map) - 1

    # Absolut positions to the neighbours
    n_pos = get_neighbour_pos(pos)

    # Handle posisions at the edge of the map
    for d,p in n_pos.items():
        xn,yn = p

        if not any([xn < 0, xn > map_x_lim, yn < 0, yn > map_y_lim]):
            n.append(get_pos_height((xn,yn),map))
        else:
            n.append(9)
            
    return n

def get_map_size(map: List[List[int]]) -> Dict[str, int]:
    return {'x': len(map[0]), 'y': len(map)}


flow_map = process_input(raw_input)
map_size = get_map_size((flow_map))

sum = 0

for y in range(0, map_size['y']):
    for x in range(0, map_size['x']):
        neighbours = get_neighbours((x,y), flow_map)
        pos_h = get_pos_height((x,y), flow_map)

        if pos_h < min(neighbours):
            sum += pos_h + 1


print(f'Part One: {sum}')

