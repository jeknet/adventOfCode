def findNumber(line):
    res = []

    for item in line:
        if item.isnumeric():
            res.append(item)

    # if len(res)<=1:
    #     return 0
    return int(res[0]+res[-1])

def recoverCalibrationValue(path):
    with open(path) as file:
        lines = file.readlines()
        
        for line in lines:
            print(line, findNumber(line))
        return sum([findNumber(value) for value in lines])

path = "challenge1.txt"

print(recoverCalibrationValue(path))
