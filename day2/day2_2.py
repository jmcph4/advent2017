def find_divisible(row):
    n = len(row)

    if n == 0 or n == 1:
        return ()

    for i in range(n):
        num = row[i]
        
        for j in range(n):
            if j == i:
                continue

            if row[j] % num == 0:
                return (max(num, row[j]), min(num, row[j]))

def sum_row_divisions(grid):
    n = len(grid)

    if n == 0 or n == 1:
        return 0

    total = 0

    for row in grid:
        divisors = find_divisible(row)
        total += divisors[0] // divisors[1]

    return total

"""
# tests
print(sum_row_divisions([[5, 9, 2, 8], [9, 4, 7 ,3], [3, 8, 6, 5]])) # 9
"""

import csv

INPUT_FILE_PATH = "input.txt"

def main():
    spreadsheet = []

    with open(INPUT_FILE_PATH, "r") as f:
        reader=csv.reader(f, delimiter='\t')

        for row in reader:
            spreadsheet.append(row)

    # convert strings to integers
    for row in spreadsheet:
        for i in range(len(row)):
            row[i] = int(row[i])

    print(sum_row_divisions(spreadsheet))
