text = input('Введите строку: ')
h_positions = [i_index for i_index in range(len(text)) if text[i_index] == 'h']
start = h_positions[0]
end = max(h_positions)
print(f'Развёрнутая последовательность между первым и последним h: {text[end - 1:start:-1]}')
