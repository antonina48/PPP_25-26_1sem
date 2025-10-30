##1. Фильтрация букв по количеству строчных и заглавных
##На вход подаётся строка, состоящая из латинских букв произвольного регистра.
##Требуется за один линейный проход (O(N)) удалить из строки все буквы, для которых количество строчных экземпляров превышает количество заглавных
##(учитывать только одну букву независимо от регистра, например, для 'a' и 'A' считать общее количество строчных и заглавных).
##В результате вернуть строку, в которой такие буквы отсутствуют вовсе (ни в строчном, ни в заглавном виде).
##Реализовать устойчивую к ошибкам обработку некорректных символов и валидацию входа.

def filter_letters(input_string):     #удаляет буквы, у которых строчных вар больше чем заглавных

    lowercase_letters_count = {}  #подсчёт строчных
    uppercase_letters_count = {}   #подсчёт заглавных
    
    for symbol in input_string:
        base_symbol = symbol.lower()  #нижн регистр
        if symbol.islower():
            lowercase_letters_count[base_symbol] = lowercase_letters_count.get(base_symbol, 0) + 1  #увелич счётчик для заглавн букв и возвр значение +1
        else:
            uppercase_letters_count[base_symbol] = uppercase_letters_count.get(base_symbol, 0) + 1
    
    #определяем буквы для удаления
    letters_to_remove = set()
    for letter in lowercase_letters_count:
        if lowercase_letters_count.get(letter, 0) > uppercase_letters_count.get(letter, 0):
            letters_to_remove.add(letter)
    
    
    result = "".join(char for char in input_string if char.lower() not in letters_to_remove) #фильтрацияя строки
    
    return result

# Пример использования
if __name__ == "__main__":
    test_input = "aCaCaAcAbcbBCBB"
    output = filter_letters(test_input)
    print(f"Input: {test_input}")
    print(f"Output: {output}")


if __name__ == "__main__":
    pass # Ваш код здесь
