def аrchiver(text: str) -> str:
    """
    В качестве алгоритма сжатия выбран алгоритм Лемпеля-Зива-Венча(LZW).
    Повторяющиеся подстроки заносятся в словарь и кодируются.
    Перед началом работы алгоритма словарь заполняется
    всеми символами, которые могут нам встретиться:
    """
    pattern_dictionaty = {chr(i): i for i in range(128)}
    """
    Далее итеративно проверяются текущий и следующий символы в строке.
    Если появляются подстроки, которых еще не было в словаре, они учитываются.
    Встречающиеся паттерны кодируются:
    """
    compressed_text: str = ''
    current_symbol: str = ''
    next_symbol: str = ''
    pattern: str = ''
    is_pattern_exist: bool = False
    counter: int = 127

    for i in range(len(text) - 1):

        if is_pattern_exist:
            current_symbol = pattern
            is_pattern_exist = False
        else:
            current_symbol = text[i]

        next_symbol = text[i + 1]
        pattern = current_symbol + next_symbol
        if pattern not in pattern_dictionaty.keys():
            counter += 1
            pattern_dictionaty[pattern] = counter
            compressed_text += chr(pattern_dictionaty[current_symbol])
        else:
            is_pattern_exist = True

    compressed_text += chr(pattern_dictionaty[text[-1]])

    return compressed_text

    """
    При декомпрессии итеративно проверяются текущий и следующий коды.
    Словарь так же динамически дополняется, при появлении новых расшифровок:
    """
def unpacker(text: str) -> str:
    codes_list = []

    for i in range(len(text)):
        codes_list.append(ord(text[i]))

    pattern_dictionaty = {chr(i): i for i in range(128)}
    decoded_text: str = ''

    def get_symbol(code: int) -> str:
        for key in pattern_dictionaty:
            if pattern_dictionaty[key] == code:
                return key
        return ''

    decoded_text += get_symbol(codes_list[0])
    current_code: int
    next_code: int
    counter: int = 127
    pattern: str = ''
    is_pattern_lost: bool = False

    for i in range(len(codes_list) - 1):
        current_code = codes_list[i]
        if is_pattern_lost:
            next_code = counter
            is_pattern_lost = False
        else:
            next_code = codes_list[i + 1]

        if next_code in pattern_dictionaty.values():
            decoded_text += get_symbol(next_code)
            pattern = get_symbol(current_code) + get_symbol(next_code)[0]
            counter += 1
            pattern_dictionaty[pattern] = counter
        else:
            counter += 1
            decoded_text += get_symbol(current_code) + get_symbol(current_code)[0]
            pattern_dictionaty[get_symbol(current_code) + get_symbol(current_code)[0]] = counter
            is_pattern_lost = True
    return decoded_text

packed = аrchiver("This 2023 string serves as 2023 example for LZW 2023 string compression method")
print("compressed string:")
print(packed)
print("unpacked string:")
print(unpacker(packed))





