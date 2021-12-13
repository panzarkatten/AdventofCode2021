from pathlib import Path

input = Path(__file__).with_name('day12_test.txt')
raw_input = input.open('r').read()

def process_input(input):
    """Process the input and return an object which is easier to work with"""
    data = [tuple(con.split('-')) for con in input.split('\n')]
    
    return data


# --- Init ---
connections = process_input(raw_input)

print(connections)
# --- Part One ---

print(f'Part One: ')


# --- Part Two ---

print(f'Part Two: ')