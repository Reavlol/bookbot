from stats import word_count
from stats import character_count, dic_sort
import sys

if len(sys.argv) !=2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

char_count = dic_sort(book_path)

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    word_count_to_print = word_count(book_path)
    print(f"Found {word_count_to_print} total words")
    print("--------- Character Count -------")
    for char, count in char_count.items():
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")

main()
