def main():
    book_path="books/frankenstein.txt"
    text=get_text(book_path)
    num_words=word_count(text)

    print (text)
    print(f"{num_words} words found")

#opens the text and returns it
def get_text(path):
    with open (path) as f:
        return f.read()


#word count for the text
def word_count(text):
    list_words=text.split()
    return len(list_words)





main()