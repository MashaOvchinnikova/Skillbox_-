def is_palindrome(num_list):
    reverse_list = num_list[::-1]
    if num_list == reverse_list:
        return True
    else:
        return False


nums = [int(input('Число: ')) for _ in range(int(input('Кол-во чисел: ')))]
answer = []

for i_nums in range(len(nums)):
    if is_palindrome(nums[i_nums:len(nums)]):
        answer = nums[:i_nums]
        answer.reverse()
        break

print(f'Последовательность: {nums}')
print(f'Нужно приписать чисел: {len(answer)}')
print(f'Сами числа: {answer}')
