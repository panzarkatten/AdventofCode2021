from pathlib import Path

input = Path(__file__).with_name('input1-1.txt')
counter = 0
prev = None
sums = []

with input.open('r') as f:
    lines = f.readlines()

    for i in range(0, len(lines)-2):
        sum = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
        sums.append(sum)

    for sum in sums:
        x = int(sum)
        if prev and x > prev:
            counter += 1
        prev = x
    else:   
        print(counter)