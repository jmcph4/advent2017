def sum_matching_digits(digits):
    total = 0
    n = len(digits)

    if n == 0:
        return total
    if n == 1:
        return digits[0]
    
    for i in range(n):
        if i == n - 1:
            if digits[i] == digits[0]:
                total += digits[i]
        else:
            if digits[i] == digits[i+1]:
                total += digits[i]

    return total

"""
# tests
print(sum_matching_digits([1, 1, 2, 2]))
print(sum_matching_digits([1, 1, 1, 1]))
print(sum_matching_digits([1, 2, 3, 4]))
print(sum_matching_digits([9, 1, 2, 1, 2, 1, 2, 9]))
"""

INPUT_FILE_PATH = "input.txt"

def main():
    digits = []

    with open(INPUT_FILE_PATH) as f:
        while True:
            c = f.read(1)

            if not c: # check for EOF
                break

            if c != "\n":
                digits.append(int(c))

    print(sum_matching_digits(digits))
