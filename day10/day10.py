from pathlib import Path

input = Path(__file__).with_name('day9.txt')
raw_input = input.open('r').read()

def process_input(input):
    """Process the input and return an object which is easier to work with"""
    data = list([list(map(int, line)) for line in list(input.strip().split('\n'))])
    
    return data



# --- Init ---
input = process_input(raw_input)

# --- Part One ---


# --- Part Two ---
