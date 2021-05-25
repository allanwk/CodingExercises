import numpy as np
import math
import itertools

class Nonogram:

    def __init__(self, clues):
        self.board = np.array([[-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1]])
        self.clues = clues
        self.col_counts = [0,0,0,0,0]
        self.row_counts = [0,0,0,0,0]
        self.xperm = [0,0,0,0,0]
        self.yperm = [0,0,0,0,0]
        print(clues)

    def solve(self):
        #Use starter clues
        for x in range(5):
            if self.clues[0][x] == (2,2):
                self.board[0][x] = 1
                self.board[1][x] = 1
                self.board[2][x] = 0
                self.board[3][x] = 1
                self.board[4][x] = 1
            elif self.clues[0][x] == (1,1,1):
                self.board[0][x] = 1
                self.board[1][x] = 0
                self.board[2][x] = 1
                self.board[3][x] = 0
                self.board[4][x] = 1
            else:
                for clue in self.clues[0][x]:
                    if clue == 5:
                        for i in range(5):
                            self.board[i][x] = 1
                    elif clue == 4:
                        self.board[1][x] = 1
                        self.board[2][x] = 1
                        self.board[3][x] = 1
                    elif clue == 3:
                        self.board[2][x] = 1
        for y in range(5):
            if self.clues[1][y] == (2,2):
                self.board[y][0] = 1
                self.board[y][1] = 1
                self.board[y][2] = 0
                self.board[y][3] = 1
                self.board[y][4] = 1
            elif self.clues[1][y] == (1,1,1):
                self.board[y][0] = 1
                self.board[y][1] = 0
                self.board[y][2] = 1
                self.board[y][3] = 0
                self.board[y][4] = 1
            else: 
                for clue in self.clues[1][y]:
                    if clue == 5:
                        for i in range(5):
                            self.board[y][i] = 1
                    elif clue == 4:
                        self.board[y][1] = 1
                        self.board[y][2] = 1
                        self.board[y][3] = 1
                    elif clue == 3:
                        self.board[y][2] = 1

        #Fill Xs
        for x in range(5):
            count = 0
            clue_sum = 0
            for y in range(5):
                if(self.board[y][x] == 1):
                    count += 1
            for clue in self.clues[0][x]:
                clue_sum += clue
            if count == clue_sum:
                for y in range(5):
                    if self.board[y][x] != 1:
                        self.board[y][x] = 0
        
        for y in range(5):
            count = 0
            clue_sum = 0
            for x in range(5):
                if(self.board[y][x] == 1):
                    count += 1
            for clue in self.clues[1][y]:
                clue_sum += clue
            if count == clue_sum:
                for x in range(5):
                    if self.board[y][x] != 1:
                        self.board[y][x] = 0
        self.count()
        self.generate()
        return tuple(map(tuple, self.board))

    def permutations(self):
        for x in range(5):
            sum = 0
            for clue in self.clues[0][x]:
                sum += clue
            self.xperm[x] = (math.factorial(len(self.clues[0][x]) + 5 - sum))/(math.factorial(len(self.clues[0][x])) * math.factorial(5 - sum))
        for y in range(5):
            sum = 0
            for clue in self.clues[1][y]:
                sum += clue
            self.yperm[y] = (math.factorial(len(self.clues[1][y]) + 5 - sum))/(math.factorial(len(self.clues[1][y])) * math.factorial(5 - sum))
    
    def count(self):
        for x in range(5):
            self.col_counts[x] = 0
            for y in range(5):
                if self.board[y][x] != -1:
                    self.col_counts[x] += 1
        for y in range(5):
            self.row_counts[y] = 0
            for x in range(5):
                if self.board[y][x] != -1:
                    self.row_counts[y] += 1

    def validate_row(self, check_row, clues):
        block_start = 0
        block_started = False
        blocks = []
        for i in range(len(check_row)):
            if check_row[i] == 1:
                if not block_started:
                    block_start = i
                    block_started = True
            elif check_row[i] == 0:
                if block_started:
                    blocks.append(i - block_start)
                    block_started = False
        if block_started:
            blocks.append(5 - block_start)
        return blocks == list(clues)



    def generate(self):
        self.permutations()
        done = False
        while done == False:
            self.count()
            checked = []
            min_perm = max(self.yperm)
            for a in range(5):
                mx = 0
                mxi = 0
                for i in range(5):
                    if self.row_counts[i] < 5 and self.row_counts[i] >= mx and i not in checked:
                        if self.row_counts[i] > mx or self.yperm[i] < min_perm:
                            mx = self.row_counts[i]
                            mxi = i
                            min_perm = self.yperm[i]
                checked.append(mxi)
                #generate all possible solutions for the best line given the constraints
                n_variables = 5 - self.row_counts[mxi]
                lst = list(itertools.product([0,1], repeat=n_variables))
                correct_scratchpad = []
                n_options = 0
                for option in lst:
                    scratchpad = self.board[mxi].copy()
                    i = 0
                    for j in range(len(scratchpad)):
                        if scratchpad[j] == -1:
                            scratchpad[j] = option[i]
                            i += 1
                    if self.validate_row(scratchpad, self.clues[1][mxi]):
                        n_options += 1
                        correct_scratchpad = scratchpad.copy()
                if n_options == 1:
                    self.board[mxi] = correct_scratchpad.copy()
                    print(self.board)
                    break

            self.count()
            checked = []
            min_perm = max(self.xperm)
            for a in range(5):
                mx = 0
                mxi = 0
                for i in range(5):
                    if self.col_counts[i] < 5 and self.col_counts[i] >= mx and i not in checked:
                        if self.col_counts[i] > mx or self.xperm[i] < min_perm:
                            mx = self.col_counts[i]
                            mxi = i
                            min_perm = self.xperm[i]
                checked.append(mxi)
                #generate all possible solutions for the best line given the constraints
                n_variables = 5 - self.col_counts[mxi]
                lst = list(itertools.product([0,1], repeat=n_variables))
                correct_scratchpad = []
                n_options = 0
                for option in lst:
                    scratchpad = [self.board[a][mxi] for a in range(5)].copy()
                    i = 0
                    for j in range(len(scratchpad)):
                        if scratchpad[j] == -1:
                            scratchpad[j] = option[i]
                            i += 1
                    if self.validate_row(scratchpad, self.clues[0][mxi]):
                        n_options += 1
                        correct_scratchpad = scratchpad.copy()
                if n_options == 1:
                    for j in range(5):
                        self.board[j][mxi] = correct_scratchpad[j]
                    print(self.board)
                    break
        
            done = True
            for x in range(5):
                for y in range(5):
                    if self.board[y][x] == -1:
                        done = False

            

                


print(Nonogram((((1, 1), (4,), (1, 1, 1), (3,), (1,)),
          ((1,), (2,), (3,), (2, 1), (4,)))).solve())