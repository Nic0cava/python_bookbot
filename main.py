from stats import get_num_words, get_num_of_chars


def main():

    def get_book_text(file_path):
        with open(file_path) as f:
            return f.read()

    file_path = "./books/frankenstein.txt"
    
    book_text = get_book_text(file_path)

    words_in_book = book_text.split()

    num_words = get_num_words(words_in_book)

    num_of_chars = get_num_of_chars(book_text)

    print(f"Found {num_words} total words")
    print(num_of_chars)


main()