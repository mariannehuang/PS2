'''
************************************************
  ____ ____    _  ___   __
 / ___/ ___|  / |/ _ \ / /_
| |   \___ \  | | (_) | '_ \
| |___ ___) | | |\__, | (_) |
 \____|____/  |_|  /_/ \___/


Problem set 1


Question 2

Given a square matrix size N x N, calculate the product of the sums across the two main diagonals.
For example, given the input:

3

4   5   7
3   1   5
9   3   2

Return: (4+1+2)*(9+1+7) = 119

PLEASE LOOK AT PS1.txt FOR MORE DETAILS!!!

************************************************
'''

def diagonal(matrix):
    numRows = len(matrix)
    numCols = len(matrix[0])
    total = 0
    for i in xrange(0, numRows):
        for j in xrange(0, numCols):
            if i == j:
                total+=int(matrix[i][j])
                if not ((i == numRows/2) and numRows%2 == 1):
                    total += int(matrix[i][numCols-j-1])
    return total

try:
    with open('Diagonal.txt') as f:
        data = f.read().split()
        num_of_tests = data[0]
        data = data[1:]

        for i in range(0, int(num_of_tests)):
            matrix = []
            dimen = int(data[0])
            data = data[1:]

            for j in range(0, dimen):
                row = data[:dimen]
                matrix.append(row)
                data = data[dimen:]
            print diagonal(matrix)
except IOError, e:
    print e
