#Kango911
def get_words_array(line):
    # Используем метод split() для разделения строки на слова по пробелам
    words = line.split()

    return words


# Пример использования функции
text = input(f'Введите строки с несколькими словами:')
words_array = get_words_array(text)
print("Массив слов в строке:")
print(words_array)
