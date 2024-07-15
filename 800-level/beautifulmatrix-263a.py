def solution():
    matrix = []
    index = []
    for i in range(0, 5):
        row = input().split(" ")
        if '1' in row:
            index.append(row.index('1'))
            index.insert(0, i)
        matrix.append(row)
    # Using the Manhattan distance formula
    print(abs(index[0] - 2) + abs(index[1] - 2))


solution()
