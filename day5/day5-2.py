from pathlib import Path
from re import findall
from math import sqrt

input = Path(__file__).with_name('day5.txt')
input = input.open('r').read()


def process_input(input):
    coords = input.replace(' ','').split('\n')
    coords = [tuple(c.split('->')) for c in coords]

    return tuple(coords)

coords = process_input(input)
# print(coords)

lines = {}
intersects = 0

for coord in coords:
    a1, b1 = coord[0].split(',')
    a2, b2 = coord[1].split(',')

    a1 = int(a1)
    a2 = int(a2)
    b1 = int(b1)
    b2 = int(b2)


    x1, y1 = min(a1,a2),min(b1,b2)
    x2, y2 = max(a1,a2),max(b1,b2)

    # print(f'x1: {x1}', end=' ')
    # print(f'y1: {y1}')
    # print(f'x2: {x2}', end=' ')
    # print(f'y2: {y2}')

    if x1 == x2 or y1 == y2:
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):        
                # print(f'x{x},y{y}')
                if (x,y) not in lines:
                    lines[(x,y)] = 0
                
                lines[(x,y)] += 1
    else:
        


for k,v in lines.items():
    if v > 1:
        intersects += 1

# print(lines)
print(len(lines))
print(lines)
print(intersects)
