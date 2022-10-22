nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
new_nice_list = [digit for second_list in nice_list for third_list in second_list for digit in third_list]
print(new_nice_list)
