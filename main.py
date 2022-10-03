import math
import os
from fractions import Fraction

def Gauss_elimination(matrix):
    """
        Returns a Echelon matrix
    """
    # to do not change the parameter

    result = []
    for line in matrix:
        array = []
        for i in line:
            array.append(i)
        result.append(array)

    row = len(result)
    col = len(result[0])

    # to fraction

    for i in range(0, row, 1):
        for j in range(0, col, 1):
            result[i][j] = Fraction(result[i][j])

    for i in range(0, row, 1):
        # find the pivot index
        pivot = 0
        isDone = True
        for j in range(i, col, 1):
            isVector0 = True
            for k in range(i, row, 1):
                if result[k][j] != 0:
                    isDone = False
                    isVector0 = False
                    break
            if not isVector0:
                pivot = j
                break
        if isDone:
            return result

        # if pivot = 0 then swap line
        if result[i][pivot] == 0:
            for j in range(i+1, row, 1):
                if result[j][pivot] != 0:
                    for k in range(pivot, col, 1):
                        result[i][k], result[j][k] = result[j][k], result[i][k]
                    break

        # if pivot is not leader
        if result[i][pivot] != 1:
            result[i] = [item * (1 / result[i][pivot]) for item in result[i]]

        for j in range(i + 1, row, 1):
            temp = result[j][pivot]
            if temp == 0:
                continue
            for k in range(pivot, col, 1):
                result[j][k] -= temp * result[i][k]

    return result


def back_substitution(matrix_echelon):
    """
        Returns root space or notice no solution
    """
    n = len(matrix_echelon)
    m = len(matrix_echelon[0])

    check = [0 for _ in range(m - 1)]
    for i in range(n):
        for j in range(m - 1):
            if matrix_echelon[i][j] == 1:
                check[j] = 1
                break
    n_x = 0
    for i in range(m - 1):
        if check[i] == 0:
            n_x = n_x + 1
    x = [[0 for _ in range(m - 1)] for _ in range(n_x + 1)]
    cnt = 0
    for i in range(len(check)):
        if check[i] == 0:
            x[cnt][i] = 1
            cnt = cnt + 1

    for i in range(n - 1, -1, -1):
        flag = 0
        for j in range(0, m - 1, 1):
            if matrix_echelon[i][j] != 0:
                flag = 1
                x[len(x) - 1][j] = matrix_echelon[i][m - 1]
                for k in range(m - 2, j, -1):
                    for s in range(len(x) - 1, -1, -1):
                        x[s][j] -= x[s][k] * matrix_echelon[i][k]
                break

        if flag == 0 and matrix_echelon[i][m - 1] != 0:
            print("the equation has no solution")
            return None
    return x


def solve(matrix):
    """
        To string
    """

    x = back_substitution(Gauss_elimination(matrix))

    if x == None:
        return
    result = ['x{} = '.format(i + 1)for i in range(len(x[0]))]
    for i in range(len(result)):
        if abs(x[len(x) - 1][i]) != 0:
            if x[len(x) - 1][i] == math.floor(x[len(x) - 1][i]):
                x[len(x) - 1][i] = int(x[len(x) - 1][i])
            result[i] += str(x[len(x) - 1][i])

    for i in range(len(x) - 1):
        for j in range(len(x[0])):
            if x[i][j] == math.floor(x[i][j]):
                x[i][j] = int(x[i][j])
            if x[i][j] > 0:
                if len(result[j]) < 6:
                    if x[i][j] != 1:
                        result[j] += '{}xa{}'.format(x[i][j], i + 1)
                    else:
                        result[j] += 'a{}'.format(i + 1)
                else:
                    if x[i][j] != 1:
                        result[j] += '+{}xa{}'.format(x[i][j], i + 1)
                    else:
                        result[j] += '+a{}'.format(i + 1)
            elif x[i][j] < 0:
                if x[i][j] != -1:
                    result[j] += '{}xa{}'.format(x[i][j], i + 1)
                else:
                    result[j] += '-a{}'.format(i + 1)

    for xi in result:
        print(xi)


if __name__ == '__main__':
    while True:
        print("row of your matrix? ")
        try:
            row = int(input("> "))
        except:
            print('please input a right format! :)')
            input('press any something to input again...')
            os.system('clear')
            continue

        print("what is your matrix? \n> ")
        try:
            matrix = [list(map(float, input().split())) for i in range(row)]
        except:
            print('your input is not a right format! :)')
            input('press any something to input again...')
            os.system('clear')
            continue
        print("-------------------")
        solve(matrix)
        input('press any something to input again...')
        os.system('clear')
