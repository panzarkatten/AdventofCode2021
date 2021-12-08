from pathlib import Path
from typing import Tuple

def process_input(input):
    lines = input.replace(' ','').split('\n')
    # cords = [c.split('->') for c in cords]
    cords = ()
    for line in lines:
        cord = line.split('->')
        cord = [tuple(map(int, c.split(','))) for c in cord]
        cords += tuple(cord)

    return tuple(cords)


def get_line_cords(cords: Tuple[Tuple[int, int], Tuple[int, int]]):
    lines = ()
    iterations = iter(cords)

    for cord in iterations:
        x1, y1 = cord
        x2, y2 = next(iterations)
        line = ()
        
        if x1 == x2 or y1 == y2:
            # Vertical or horizontal line
            x1, x2 = min(x1,x2),max(x1,x2)
            y1, y2 = min(y1,y2),max(y1,y2)

            for x in range(x1,x2+1):
                for y in range(y1,y2+1):        
                    # print(f'x{x},y{y}')
                    line += ((x,y),)
        else:
            # Diagonal line
            if x1 < x2:
                xstep = 1
                x2 += 1
            else:
                xstep = -1
                x2 -= 1

            if y1 < y2:
                ystep = 1
                y2 += 1
            else:
                ystep = -1
                y2 -= 1

            x = list(range(x1, x2, xstep))
            y = list(range(y1, y2, ystep))

            line = tuple(zip(x,y))
        
        lines += (line,)
    
    return lines

# Takes two lines and returns the coordinate where they intersect. Returns None if they don't intersect
def get_line_intersects(lines):
    intersects = {}
    for line in lines:
        for cord in line:
            x,y = cord
            if (x,y) not in intersects:
                intersects[(x,y)] = 0
            
            intersects[(x,y)] += 1
    
    return [k for k,v in intersects.items() if v > 1]


input = Path(__file__).with_name('day5.txt')
input = input.open('r').read()

cords = process_input(input)

lines = get_line_cords(cords)
intersections = get_line_intersects(lines)

print(len(intersections))