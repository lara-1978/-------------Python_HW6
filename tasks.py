# Задание 1.
# Модуль для подсчета количества повторений слов
# Создайте модуль с функцией, которая получает список слов и возвращает
# словарь, в котором ключи — это слова, а значения — количество их повторений в списке.


# variant1

# def word_frequency(word_list):
#     """
#     Returns a dictionary with word frequencies.
#
#     Args:
#         word_list (list): A list of words.
#
#     Returns:
#         dict: A dictionary where keys are words and values are their frequencies.
#     """
#     frequency_dict = {}
#     for word in word_list:
#         if word in frequency_dict:
#             frequency_dict[word] += 1
#         else:
#             frequency_dict[word] = 1
#     return frequency_dict
#

# variant2

import word_count
def count_word_occurrences(words):

    word_count = {}
    for word in words:

        [word] = word_count.get(word, 0) + 1
# Возвращаем словарь с количеством повторений слов
        return word_count

print(word_count.count_word_occurrences(['apple', 'banana', 'apple', 'orange']))

# Output: {'apple': 2, 'banana': 1, 'orange': 1}


# Задача 2. Модуль для удаления дублирующихся подряд символов
# Напишите модуль с функцией, которая принимает строку и возвращает строку с
# удаленными дублирующимися подряд идущими символами. Например, строка "aabbccaa" должна быть преобразована в "abca".





def remove_consecutive_duplicates(input_string):

    result_string = ""
    for char in input_string:
        if not result_string or char != result_string[-1]:
            result_string += char
    return result_string

input_str = "aabbccaa"
output_str = remove_consecutive_duplicates(input_str)
print(output_str)  # Output: "abca"


