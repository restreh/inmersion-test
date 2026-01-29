def zero_cleaning(nums):
    non_zero_elements = [num for num in nums if num != 0]
    zero_count = len(nums) - len(non_zero_elements)
    return non_zero_elements + ([0]*zero_count)


test = [4, 1, 2, 0, 0, 0, 3, 0, 5]

result = zero_cleaning(test)
print(result)