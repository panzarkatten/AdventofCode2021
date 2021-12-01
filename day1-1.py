from pathlib import Path

input = Path(__file__).with_name('input1-1.txt')
prev = None
counter = 0

with input.open('r') as f:
    lines = f.readlines()
    
    for line in lines:
        x = int(line)
        if prev and x > prev:
            counter += 1
        prev = x
    else:   
        print(counter)
