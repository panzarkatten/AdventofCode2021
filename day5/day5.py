from pathlib import Path
from re import findall
from math import sqrt

def process_input(input):
    coords = input.replace(' ','').split('\n')
    coords = [tuple(c.split('->')) for c in coords]

    return tuple(coords)

input = Path(__file__).with_name('day5.txt')
input = input.open('r').read()

coords = process_input(input)

lines = {}
intersects = 0

for coord in coords:
    a1, b1 = coord[0].split(',')
    a2, b2 = coord[1].split(',')

    a1 = int(a1)
    a2 = int(a2)
    b1 = int(b1)
    b2 = int(b2)

    if a1 == a2 or b1 == b2:
        x1, x2 = min(a1,a2),max(a1,a2)
        y1, y2 = min(b1,b2),max(b1,b2)

        for x in range(x1,x2+1):
            for y in range(y1,y2+1):        
                # print(f'x{x},y{y}')
                if (x,y) not in lines:
                    lines[(x,y)] = 0
                
                lines[(x,y)] += 1


for k,v in lines.items():
    if v > 1:
        intersects += 1


print(intersects)
