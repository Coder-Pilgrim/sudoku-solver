import grid as grid
import numpy as numPy

grid = [[0, 0, 6, 3, 0, 7, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 5],
        [1, 0, 0, 0, 0, 6, 0, 8, 2],
        [2, 0, 5, 0, 3, 0, 1, 0, 6],
        [0, 0, 0, 2, 0, 0, 3, 0, 0],
        [9, 0, 0, 0, 7, 0, 0, 0, 4],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 1, 0, 9, 0, 4, 0]]


print(numPy.matrix(grid))


def isPossible(x, y, z):  # x and y are locations of the matrix, z is the number to be checked
    if z > 9 or z < 0:
        print("Error: Number is out of range")

    for i in range(0, 9):
        if grid[x][i] == z:
            return False
    for i in range(0, 9):
        if grid[i][y] == z:
            return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[x0 + i][y0 + j] == z:
                return False
    return True


# print(isPossible(0, 2, 4))


def solve():
    for i in range(0, 9):
        for j in range(0, 9):
            if grid[i][j] == 0:
                #print("Empty cell at: ", i, j)
                for k in range(1, 10):
                    if isPossible(i, j, k):
                        #print("Number", k, "is possible at", i, j)
                        grid[i][j] = k
                        solve()
                        grid[i][j] = 0
                        #print("Backtracking")
                return False
    print(numPy.matrix(grid))


print("Solving...")
solve()
print("Solved.")
