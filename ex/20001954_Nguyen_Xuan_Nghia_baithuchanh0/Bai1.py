def findSaddlePoint(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    exist = False

    for rowRun in range(rows):
        minInRowValue = minInRow(matrix[rowRun])

        for col in range(cols):
            maxInColumnValue = matrix[0][col]

            for row in range(rows):
                if maxInColumnValue < matrix[row][col]:
                    maxInColumnValue = matrix[row][col]

            if (maxInColumnValue == minInRowValue):
                exist = True
                print("saddle point is: ", maxInColumnValue)

    if not exist:
        print("Matrix does not have saddle point")

def minInRow(rows):
    minInRow = rows[0]

    for row in range(len(rows)):
        if (minInRow > rows[row]):
            minInRow = rows[row]

    return minInRow

findSaddlePoint([[1,2,3],
                [4,5,6],
                [7,8,9]])


