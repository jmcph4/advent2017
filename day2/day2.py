def row_diff(row):
    n = len(row)

    if n == 0 or n == 1:
        return 0

    return max(row) - min(row)

def checksum(grid):
    total = 0
    n = len(grid)

    if n == 0:
        return 0
    
    for row in grid:
        total += row_diff(row)

    return total

"""
# tests
print(checksum([[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]])) # 18
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

    print(checksum(spreadsheet))
