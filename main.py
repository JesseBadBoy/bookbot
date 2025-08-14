from stats import count_words, get_book_text, count_chars, sort_dict
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_to_analyze = sys.argv[1]
    #print(get_book_text(book_to_analyze))
    word_count = count_words(get_book_text(book_to_analyze))


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_to_analyze}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    preped_chars = sort_dict(count_chars(get_book_text(book_to_analyze)))
    for i in preped_chars:
        print(f"{i['char']}: {i['num']}")
    
    print("============= END ===============")
    
main()