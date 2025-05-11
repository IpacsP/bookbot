import sys
from stats import get_num_words, get_char_count, char_sorted

def get_book_text(book_path):
    with open(book_path, 'r') as file:
        book_text = file.read()
    return book_text

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    sorted_list = char_sorted(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for c in sorted_list:
        print(f"{c["char"]}: {c["count"]}")
    print("============= END ===============")