from pathlib import Path

input = Path(__file__).with_name('input1-1.txt')
lines = input.open('r').readlines()

def depthIncrease (data):
    depthinc = 0
    prev = None
    for depth in data:
        depth = int(depth)
        if prev and depth > prev:
            depthinc += 1
        prev = depth

    return depthinc

def depthIncreaseFiltered (data):
    filteredData = []
    for i in range(0, len(data)-2):
        sum = int(data[i]) + int(data[i+1]) + int(data[i+2])
        filteredData.append(sum)
    
    return depthIncrease(filteredData)


print("Depth increased:" + str(depthIncrease(lines)))
print("Depth increased Filtered:" + str(depthIncreaseFiltered(lines)))