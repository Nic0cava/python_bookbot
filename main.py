from stats import get_num_words, get_num_of_chars, create_char_list
import sys

def main():

    def get_book_text(file_path):
        with open(file_path) as f:
            return f.read()

    def sort_on(items):
        return items["num"]
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = f"./{sys.argv[1]}"
    
    book_text = get_book_text(file_path)

    words_in_book = book_text.split()

    num_words = get_num_words(words_in_book)

    num_of_chars = get_num_of_chars(book_text)

    char_list = create_char_list(num_of_chars)

    char_list.sort(reverse=True, key=sort_on)

    # REPORT
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path[2:]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in char_list:
        char = item["char"]
        num = item["num"]
        if char.isalpha():
            print(f"{char}: {num}")
    print("============= END ===============")

main()