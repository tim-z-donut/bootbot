
from stats import get_book_text
from stats import get_num_words
from stats import get_num_chars
from stats import sort_count
import sys


def main():
    
    arguments = sys.argv
    if len(arguments) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    for book in arguments[1:]:

        # print(f"Analyzing: {book}")
        string = get_book_text(book)



        print(get_num_words(string))
        # print()
        counts:dict = get_num_chars(string)
        # return counts
        print(sort_count(counts))

main()

# d.sort(key=)