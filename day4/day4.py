from pathlib import Path
from re import findall
from math import sqrt

input = Path(__file__).with_name('day4.txt')
lines = input.open('r').read().split('\n\n')

class bingo_board():
    def __init__(self, numbers, index) -> None:
        self.index = index
        self.marked = [False] * 25
        self.numbers = findall('\d+', numbers)
        for i in range(0, len(self.numbers)):
            self.numbers[i] = int(self.numbers[i])

        self.size = int(sqrt(len(self.numbers)))
    
    # Method to mark a number on the board. 
    def mark(self, num):
        if num in self.numbers:
            self.marked[self.numbers.index(num)] = True
    
    # Evaluate if the board has a row och column fully marked
    def bingo(self):
        bingo = []
        for i in range(0, self.size):
            bingo.append(all(self._mrow(i)))
            bingo.append(all(self._mcol(i)))
        
        assert len(bingo) == self.size * 2
        
        return any(bingo)

    # Get all unmarked numbers in the board
    def all_unmarked(self):
        board = dict(zip(self.numbers, self.marked))
        return [num for num, marked in board.items() if not marked]

    # Return marked row number n
    def _mrow(self, n):
        start = n * self.size
        end = start + self.size
        return self.marked[start:end]
    
    # Return marked column number n
    def _mcol(self, n):
        return self.marked[n::self.size]

# Draw the balls and mark the numbers drawn on each board
def play_bingo(balls, boards):
    for ball in balls:
        ball = int(ball)
        for board in boards:
            board.mark(ball)
            if board.bingo():
                return sum(board.all_unmarked()) * ball

def play_last_bingo(balls, boards):
    winning_boards = set()
    for ball in balls:
        ball = int(ball)
        for board in boards:
            board.mark(ball)
            if board.bingo():
                winning_boards.add(board.index)
                if len(winning_boards) == len(boards):
                    return sum(board.all_unmarked()) * ball

# Create bingo boards
boards = []
for i in range(1, len(lines)):
    boards.append(bingo_board(lines[i], i - 1))

# Create balls
balls = lines[0].split(',')

print('Score part 1: ' + str(play_bingo(balls, boards)))
print('Score part 2: ' + str(play_last_bingo(balls, boards)))
