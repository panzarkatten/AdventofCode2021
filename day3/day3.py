from pathlib import Path

input = Path(__file__).with_name('day3.txt')
lines = input.open('r').read().split('\n')

def is_bit_on(bits, n):
    testbit = '0' * len(bits)
    testbit = testbit[:n] + '1' + testbit[n+1:]
    
    if int(testbit, 2) & int(bits, 2):
        return True
    else:
        return False


def n_bit_freq(bitlist, n, least = False):
    n_bits = []
    freq_bit = None
    
    for bits in bitlist:
        n_bits.append(is_bit_on(bits, n))

    if least:
        if n_bits.count(not least) <= n_bits.count(least):
            freq_bit = '0'
        else:
            freq_bit = '1'
    else:
        if n_bits.count(not least) >= n_bits.count(least):
            freq_bit = '1'
        else:
            freq_bit = '0'

    return freq_bit


def filter_bitlist(bitlist, least = False):
    new_bitlist = bitlist
    for i in range(0, len(bitlist[0])):
        bitlist = new_bitlist
        new_bitlist = []
        save_bit = n_bit_freq(bitlist, i, least)
        
        for j in range(0, len(bitlist)):
            if bitlist[j][i] == save_bit:
                new_bitlist.append(bitlist[j])

        if len(new_bitlist) == 1:
            break

    assert len(new_bitlist) == 1

    return new_bitlist[0]

bitlen = len(lines[0])
gamma = ''
for i in range(0, bitlen):
    gamma += n_bit_freq(lines, i)

gamma = int(gamma, 2)
epsilon = gamma ^ int(('1' * bitlen), 2)
power = gamma * epsilon

print('--- Part 1 ---')
print('Gamma: ' + str(gamma))
print('Epsilon: ' + str(epsilon))
print('Power Consumption: ' + str(power))

oxygen = int(filter_bitlist(lines), 2)
co2 = int(filter_bitlist(lines, True), 2)
life_support = oxygen * co2

print('--- Part 2 ---')
print('Oxygen: ' + str(oxygen))
print('CO2: ' + str(co2))
print('Life Support: ' + str(life_support))