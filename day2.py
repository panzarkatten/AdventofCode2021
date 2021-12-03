from pathlib import Path

input = Path(__file__).with_name('day2.txt')
lines = input.open('r').readlines()

def dive (data):
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

def dive_aim (data):
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


print('Dive: ' + str(dive(lines)))
print('Dive Aim: ' + str(dive_aim(lines)))