from pathlib import Path
from typing import Tuple, List

def process_input(input: str) -> List[Tuple[Tuple[str, str], Tuple[str, str]]]:
    """Process the input and return an object which is easier to work with"""

    lines = input.strip().split('\n')
    data = []
    
    for line in lines:
        pattern, output = line.split('|')

        data.append((tuple(pattern.split()),tuple(output.split())))

    return data

def pattern_to_bits(pattern):
    conv = {
        'a': 0, 
        'b' : 1, 
        'c' : 2, 
        'd' : 3, 
        'e' : 4, 
        'f' : 5, 
        'g' : 6
    }

    bits = [0] * 7
    ref_pattern = 'abcdefg'

    pattern = sorted(pattern)

    for c in pattern:
        bits[conv[c]] = 1

    return bits

def str_diff(a: str, b: str) -> Tuple[str, str]:
    a_diff = ''
    b_diff = ''
    
    for c in a:
        if b.count(c) == 0:
            a_diff += c

    for c in b:
        if a.count(c) == 0:
            b_diff += c
    
    return tuple((a_diff, b_diff))

input = Path(__file__).with_name('day8_test.txt')
raw_input = input.open('r').read()

SS = process_input(raw_input)

a = 'bdegc'
b = 'abdfec'

print(str_diff(a,b))

""" 
bit_conv_patterns = []

for s in SS:
    PS, OS = s
    bit_patterns = []
    for p in PS:
        bit_p = pattern_to_bits(p)
        bit_patterns.append(bit_p)
        print(p,bit_p,sep='\t\t:\t', end='\n')
    
    bit_conv_patterns.append(bit_patterns)
 

    print('\n')


for digit in bit_conv_patterns[0]:
    if digit.count(1) == 2:
        print(digit)
 """
