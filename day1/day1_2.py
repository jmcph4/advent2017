def sum_matching_digits(digits):
    total = 0
    n = len(digits)

    if n == 0:
        return total
    if n == 1:
        return digits[0]

    shift = n // 2 # how far forward to look
    
    for i in range(n):
        if digits[i] == digits[(i+shift)%n]:
            total += digits[i]

    return total

"""
# tests
print(sum_matching_digits([1, 2, 1, 2])) # 6
print(sum_matching_digits([1, 2, 2, 1])) # 0
print(sum_matching_digits([1, 2, 3, 4, 2, 5])) # 4
print(sum_matching_digits([1, 2, 1, 3, 1, 4, 1, 5])) # 4
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
