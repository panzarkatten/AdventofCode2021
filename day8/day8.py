from pathlib import Path
from typing import Tuple, List, Dict

input = Path(__file__).with_name('day8.txt')
raw_input = input.open('r').read()

def process_input(input: str) -> List[Tuple[Tuple[str, str], Tuple[str, str]]]:
    """Process the input and return an object which is easier to work with"""

    lines = input.strip().split('\n')
    data = []
    
    for line in lines:
        pattern, output = line.split('|')

        data.append((tuple(pattern.split()),tuple(output.split())))

    return data

def decode_easy_patterns(patterns: Tuple[str, str]) -> Dict:
    easy_digits_len = [2, 3, 4, 7]

    decoded_patterns = {}

    for p in patterns:
        if easy_digits_len.count(len(p)) > 0:    
            p_len = len(p)
            if p_len == 2:
                digit = 1
            elif p_len == 3:
                digit = 7
            elif p_len == 4:
                digit = 4
            else:
                digit = 8

            decoded_patterns[p] = digit

    return decoded_patterns

input = process_input(raw_input)
easy_digits_len = [2, 3, 4, 7]
counter = 0

for signal in input:
    patterns, outputs = signal
    
    decoded_patterns = decode_easy_patterns(patterns)

    print(decoded_patterns)

    for o in outputs:
        if o in decoded_patterns:
            counter += 1

print(f'1,4,7,8 occur {counter} times')