from collections import defaultdict

def day08(out):
    count = 0
    for line in out:
        for item in line.split(' '):
            if len(item) in (2,3,4,7):
                count += 1
    return count

def day08_2(output):
    num = []
    for o in output.split():
        size = len(o)
        s = set(o)
        if size == 2:
            num.append("1")
        elif size == 3:
            num.append("7")
        elif size == 4:
            num.append("4")
        elif size == 7:
            num.append("8")
        elif size == 5:
            if len(s & d[2]) == 2:
                num.append("3")
            elif len(s & d[4]) == 2:
                num.append("2")
            else:
                num.append("5")
        else:
            if len(s & d[2]) == 1:
                num.append("6")
            elif len(s & d[4]) == 4:
                num.append("9")
            else:
                num.append("0")
    return int(''.join(num))

if __name__ == "__main__":
    with open('./input.txt') as f:
        data = f.read().splitlines()
        res = 0
        for line in data:
            signal, output = line.strip().split(" | ")
            d = defaultdict()

            for s in signal.split():
                val = set(s)
                if len(val) in (2, 4):
                    d[len(val)] = val

            res += day08_2(output)
        print(res)