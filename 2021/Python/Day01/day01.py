
def measurement(data):
    count = 0
    for i in range(1, len(data)):
        if data[i-1] < data[i]:
            count+=1
    return count


def measurement2(data):
    count = 0
    for i in range(len(data)):
        win1 = sum(data[i:i+3])
        win2 = sum(data[i+1:i+4])
        if win1 < win2:
            count += 1
    return count


if __name__ == "__main__":
    with open('./input.txt') as f:
        data = f.read().split()
        data = list(map(int, data))
    result = measurement2(data)
    print(result)