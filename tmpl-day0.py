from pathlib import Path

input = Path(__file__).with_name('input.txt')

with input.open('r') as f:
    lines = f.readlines()

    for line in lines:

    
print(lines)