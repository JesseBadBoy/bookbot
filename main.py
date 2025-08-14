from stats import count_words, get_book_text, count_chars, sort_dict

def main():

    book_to_analyze = "frankenstein"
    #print(get_book_text(book_to_analyze))
    word_count = count_words(get_book_text(book_to_analyze))


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/{book_to_analyze}.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    preped_chars = sort_dict(count_chars(get_book_text(book_to_analyze)))
    for i in preped_chars:
        print(f"{i['char']}: {i['num']}")
    
    print("============= END ===============")
    
main()