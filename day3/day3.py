from pathlib import Path

input = Path(__file__).with_name('day3.txt')
lines = input.open('r').readlines()
counter = [0] * (len(lines[0])-1)
gamma = ''
epsilon = ''


for line in lines:
    x = line.strip()
    for i in range(0, len(x)):
        #print(x[i:i+1])
        counter[i] += int(x[i:i+1])

for x in counter:
    if x >= len(lines)/2:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print(gamma + ' = ' + str(int(gamma, 2)))
print(epsilon + ' = ' + str(int(epsilon, 2)))
print('Power Consumption: ' + str(int(gamma, 2) * int(epsilon, 2)))
