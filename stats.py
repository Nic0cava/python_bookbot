def get_num_words(list_of_words):
    return len(list_of_words)

def get_num_of_chars(book_text):
    char_count = {}
    for char in book_text.lower():
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1
    return char_count

def create_char_list(num_of_chars):
    char_list = []
    for char, num in num_of_chars.items():
        char_dict = {}
        char_dict["char"] = char
        char_dict["num"] = num
        char_list.append(char_dict)
    return char_list