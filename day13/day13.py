from pathlib import Path

input = Path(__file__).with_name('day13_test.txt')
raw_input = input.open('r').read()

def process_input(input):
    """Process the input and return an object which is easier to work with"""
    data = input.split('\n\n')

    in1 = data[0].split('\n')
    dots = []
    for dot in in1:
        x,y = dot.split(',')
        x = int(x)
        y = int(y)
        dots.append(tuple((x,y)))

    in2 = data[1].split('\n')
    folds = []
    for fold in in2:
        d,n = fold.split()[2].split('=')
        n = int(n)
        folds.append(tuple((d,n)))

    return dots, folds

      

# --- Init ---
dots, folds = process_input(raw_input)

print(dots, folds, sep='\n')
# --- Part One ---

print(f'Part One: ')


# --- Part Two ---

print(f'Part Two: ')