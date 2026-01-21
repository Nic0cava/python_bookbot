def main():

    def get_book_text(file_path):
        with open(file_path) as f:
            return f.read()
        
    def get_num_words(list_of_words):
        return len(list_of_words)

    file_path = "./books/frankenstein.txt"
    
    book_text = get_book_text(file_path)

    words_in_book = book_text.split()

    num_words = get_num_words(words_in_book)

    print(f"Found {num_words} total words")


main()