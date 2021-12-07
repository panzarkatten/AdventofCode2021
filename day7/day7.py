from pathlib import Path

input = Path(__file__).with_name('day7.txt')
input = input.open('r').read()

def process_input(input):
    x = input.strip().split(',')
    for i in range(0,len(x)):
        x[i] = int(x[i])
    
    return x

crab_positions = process_input(input)

def calculate_fuel(crab_positions, target):
    fuel = 0
    for pos in crab_positions:
        fuel += abs(pos - target)

    return fuel

def calculate_fuel_2(crab_positions, target):
    fuel = 0
    for pos in crab_positions:
        cur_fuel = 0
        for i in range(1, abs(pos - target) + 1):
            cur_fuel += i

        fuel += cur_fuel
    
    return fuel


min_pos = min(crab_positions)
max_pos = max(crab_positions)

fuel_calculations = []
fuel_calculations_2 = []

for i in range(min_pos, max_pos):
    fuel_calculations += [calculate_fuel(crab_positions, i)]
    fuel_calculations_2 += [calculate_fuel_2(crab_positions, i)]

print(f'Minimum fuel acc. to my calcualtions: {min(fuel_calculations)}')
print(f'Minimum fuel acc. to the crabs calcualtions: {min(fuel_calculations_2)}')