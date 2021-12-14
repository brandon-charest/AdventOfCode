
def part1(data):
    def get_cost(pos, x):
        temp = 0
        for i in pos:
            temp += abs(x - i)
        return temp

    minVal = min(data)
    maxVal = max(data)

    lowCost = float('inf')

    for i in range(minVal, maxVal + 1):
        cost = get_cost(data, i)
        if cost < lowCost:
            lowCost = cost
    return lowCost

def part2(data):
    def get_cost(pos, x):
        dist = 0
        cost = 0
        for i in pos:
            dist = abs(x - i)
            cost += (dist * (dist + 1)) // 2
        return cost

    minVal = min(data)
    maxVal = max(data)

    lowCost = float('inf')

    for i in range(minVal, maxVal + 1):
        cost = get_cost(data, i)
        if cost < lowCost:
            lowCost = cost
    return lowCost



if __name__ == "__main__":
    with open('./input.txt') as f:
        data = list(map(int,f.read().split(',')))
        print(part2(data))