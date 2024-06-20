def swap_adjacent_chars(line):
    # Преобразуем строку в список символов, чтобы можно было менять элементы местами
    chars = list(line)

    # Проходим по строке и меняем местами соседние символы
    for i in range(0, len(chars) - 1, 2):
        chars[i], chars[i + 1] = chars[i + 1], chars[i]

    # Собираем список символов обратно в строку
    swapped_line = ''.join(chars)

    return swapped_line


# Пример использования функции
text = input(f'Введите строки:')
swapped_text = swap_adjacent_chars(text)
print("Исходная строка:")
print(text)
print("\nСтрока после замены рядом стоящих символов:")
print(swapped_text)
