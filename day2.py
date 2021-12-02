from pathlib import Path

input = Path(__file__).with_name('input2.txt')
lines = input.open('r').readlines()

def diveSimple (data):
    depth = 0
    hpos = 0

    for command in data:
        dir, steps = command.strip().rsplit()
        steps = int(steps)
        if dir == 'forward':
            hpos += steps
        elif dir == 'down':
            depth += steps
        elif dir == 'up':
            depth -= steps
        else:
            print('No command found')

    return depth * hpos

def diveComplex (data):
    depth = 0
    hpos = 0
    aim = 0

    for command in data:
        dir, steps = command.strip().rsplit()
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
        
    return depth * hpos


print('Dive version 1 result: ' + str(diveSimple(lines)))
print('Dive version 2 result: ' + str(diveComplex(lines)))