from pathlib import Path

input = Path(__file__).with_name('day14_test.txt')
raw_input = input.open('r').read()

def process_input(input):
    """Process the input and return an object which is easier to work with"""
    template, pairs = input.split('\n\n')

    pairs = [tuple(con.split(' -> ')) for con in pairs.split('\n')]
    
    return template, pairs


# --- Init ---
tpl, prs = process_input(raw_input)

print(tpl, prs, sep='\n')
# --- Part One ---

print(f'Part One: ')


# --- Part Two ---

print(f'Part Two: ')