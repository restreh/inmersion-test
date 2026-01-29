def find_single_number(numbers):
    if len(numbers) % 2 == 0:
        print("There should be an odd number of elements so that there is one that is unique.")
        return
    
    result = 0
    for num in numbers:
        result ^= num
    
    print(result)

find_single_number([1, 1, 2, 2, 3, 4, 4])