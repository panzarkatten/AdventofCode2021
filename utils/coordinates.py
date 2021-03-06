from typing import Tuple

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

def get_line_intersects(lines):
    intersects = {}
    for line in lines:
        for cord in line:
            x,y = cord
            if (x,y) not in intersects:
                intersects[(x,y)] = 0
            
            intersects[(x,y)] += 1
    
    return [k for k,v in intersects.items() if v > 1]
