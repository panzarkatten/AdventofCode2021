from pathlib import Path

input = Path(__file__).with_name('input.txt')
lines = input.open('r').readlines()

for line in lines:
    x = line.strip().split()
    
print(lines)