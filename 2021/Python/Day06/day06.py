from collections import defaultdict

def simulate(data, days):
    d = defaultdict(int)

    for x in data:
        d[x] += 1

    for _ in range(days):
        fish = defaultdict(int)
        for k,v in d.items():
            if k == 0:
                fish[8] += v
                fish[6] += v
            else:
                fish[k-1] += v
        d = fish


    return sum(d.values())



if __name__ == "__main__":
    with open('./input.txt') as f:
        data = list(map(int,f.read().split(',')))
        print(simulate(data,256))
