

def diveCalc(data):
    h,d = 0,0
    for command in data:
        direction, val = command.split()
        if direction == 'forward':
            h += int(val)
        elif direction == 'up':
            d -= int(val)
        elif direction == 'down':
            d += int(val)
    return h * d


def diveCalc2(data):
    h,d,a = 0,0,0
    for command in data:
        direction, val = command.split()
        if direction == 'forward':
            h += int(val)
            d += a * int(val)
        elif direction == 'up':
            a -= int(val)
        elif direction == 'down':
            a += int(val)
    return h * d



if __name__ == "__main__":
    with open('./input.txt') as f:
        data = list(f.read().splitlines())
    result = diveCalc2(data)
    print(result)