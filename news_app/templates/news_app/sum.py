numbers = [5, 3, 8, 1, 9]
min_num = numbers[0]  # Предположим, что первый элемент минимальный
for num in numbers:
    if num < min_num:
        min_num = num
print("Наименьший элемент в списке:", min_num)
