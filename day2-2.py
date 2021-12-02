from pathlib import Path

input = Path(__file__).with_name('input2-1.txt')
lines = input.open('r').readlines()

depth = 0
hpos = 0
aim = 0

for line in lines:
    dir, steps = line.strip().rsplit(' ')
    steps = int(steps)
    if dir == 'forward':
        depth += steps * aim
        hpos += steps
    elif dir == 'down':
        aim += steps
    elif dir == 'up':
        aim -= steps
    else:
        print('No command found')
    
print(depth * hpos)