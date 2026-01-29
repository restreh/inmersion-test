def find_missing_number(numbers, n):

    for i in range(1, n + 1):
        if i not in numbers:
            return i

test = [1, 2, 4, 5]
n = 5

result = find_missing_number(test, n)
print(result)  # Output: 3