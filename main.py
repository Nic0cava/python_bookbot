from stats import get_num_words


def main():

    def get_book_text(file_path):
        with open(file_path) as f:
            return f.read()

    file_path = "./books/frankenstein.txt"
    
    book_text = get_book_text(file_path)

    words_in_book = book_text.split()

    num_words = get_num_words(words_in_book)

    print(f"Found {num_words} total words")


main()