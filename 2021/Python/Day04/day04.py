from itertools import groupby

class BingoCell:
    marked = False

    def __init__(self, number):
        self.number = number

    def mark(self):
        self.marked = True

    def __repr__(self):
        return str(self.number)

class BingoCard:
    def __init__(self, data: list[list[BingoCell]]):
        self.data = data

    @classmethod
    def create(cls, data: list[str]):
        card = [[BingoCell(int(x)) for x in line.split()] for line in data]
        return cls(card)

    def mark(self, num):
        for row in self.data:
            for cell in row:
                if cell.number == num:
                    cell.mark()

    def winner(self):
        for row in self.data:
            if all(cell.marked for cell in row):
                return True
        return any(all(cell.marked for cell in col) for col in zip(*self.data))

    def unmarked_sum(self):
        sum = 0
        for row in self.data:
            for cell in row:
                if not cell.marked:
                    sum += cell.number
        return sum

    def __repr__(self):
        return str(self.data)

    
class Day04:
    def __init__(self, call_numbers: list[int], boards: list[BingoCard]):
        self.call_numbers = call_numbers
        self.boards = boards

    def solve(self, last=False):

        def is_last_winner(boards):
            return sum(not board.winner() for board in boards) == 0

        if not last:
            for number in self.call_numbers:
                for board in self.boards:
                    board.mark(number)

                    if board.winner():
                        print(board.unmarked_sum() * number)
                        return
        else:
            for number in self.call_numbers:
                for board in self.boards:
                    if board.winner():
                        continue

                    board.mark(number)
                    if board.winner() and is_last_winner(self.boards):
                        print(board.unmarked_sum() * number)
                        return


if __name__ == "__main__":
    with open('./input.txt') as f:
        data = f.read().splitlines()
        lines = [list(y) for x,y in groupby(data, key=lambda x: x!="") if x]
        call_numbers = [int(x) for x in lines.pop(0)[0].split(",")]
        boards = [BingoCard.create(x) for x in lines]
        day04 = Day04(call_numbers, boards)
        day04.solve(last=True)


