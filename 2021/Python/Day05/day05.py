class Day05:

    def __init__(self, input):
        self.pointList = [[x for x in y.split(' -> ')] for y in input]
        self.points = {}

    def diag_enumurator(self, x1,y1,x2,y2):
        x = x1
        y = y1
        delta_x = 1 if x1 < x2 else -1
        delta_y = 1 if y1 < y2 else -1

        while x != x2:
            yield x, y
            x += delta_x
            y += delta_y
        yield x, y

    def _helper(self, line):
        x1, y1 = map(int, line[0].strip().split(','))
        x2, y2 = map(int, line[1].strip().split(','))

        if x1 < x2 or y1 < y2:
            return x1, y1, x2, y2
        else:
            return x2, y2, x1, y1


    def solve(self):
        for item in self.pointList:
            x1, y1, x2, y2 = self._helper(item)

            if x1 == x2 or y1 == y2:
                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
                        if (x,y) in self.points:
                            self.points[(x,y)] += 1
                        else:
                            self.points[(x,y)] = 1
            else:
                for x, y in self.diag_enumurator(x1,y1,x2,y2):
                    if (x,y) in self.points:
                        self.points[(x,y)] += 1
                    else:
                        self.points[(x,y)] = 1
        count = 0
        for k in self.points.keys():
            if self.points[k] > 1:
                count += 1
        return count


if __name__ == "__main__":
    with open('./input.txt') as f:
        data = f.read().splitlines()
        d5 = Day05(data)
        print(d5.solve())

