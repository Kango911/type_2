def remove_first_word(line):
    # Разделяем строку на слова по пробелам
    words = line.split()

    # Удаляем первое слово (если оно есть)
    if words:
        del words[0]

    # Соединяем слова обратно в строку
    result = ' '.join(words)

    return result


# Пример использования функции
text = input(f'Введите строку:')
new_text = remove_first_word(text)
print("Исходная строка:")
print(text)
print("\nСтрока после удаления первого слова:")
print(new_text)
