import sys
from stats import count_words, count_characters, sorted_dict

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    
    text = get_book_text(book_path)
    num_words = count_words(text)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    chars = count_characters(text)
    sorted_chars = sorted_dict(chars)
    
    for entry in sorted_chars:
        if entry["char"].isalpha():
            print(f"{entry['char']}: {entry['num']}")
    
    print("============= END ===============")

main()