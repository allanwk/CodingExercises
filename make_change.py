import numpy as np
def count_change(money, coins):
    matrix = [[0 for i in range(money + 1)] for j in range(len(coins) + 1)]
    matrix = np.array(matrix)
    for i in range(len(coins) + 1):
        matrix[i][0] = 1
    for y in range(1, len(coins) + 1):
        c = coins[:y]
        for x in range(money + 1):
            if c[-1] <= x:
                matrix[y][x] = matrix[y-1][x] + matrix[y][x-c[-1]]
            else:
                matrix[y][x] = matrix[y-1][x]
    return matrix[-1][-1]