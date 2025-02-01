def main():
    book_path="books/frankenstein.txt"
    text=get_text(book_path)
    num_words=word_count(text)
    letter_count=char_count(text)

    #print (text)
    print(f"{num_words} words found")
    print(letter_count)
    return

#opens the text and returns it
def get_text(path):
    with open (path) as f:
        return f.read()

#word count for the text
def word_count(text):
    list_words=text.split()
    return len(list_words)

#counts each character in the text returns a dictionary of {'char': int}
def char_count(text):
    count_dict={}
    lowered_text=text.lower()
    char_list=list(lowered_text)

    #add keys to the dictionary and increase by 1
    for char in char_list:
        if char in count_dict == False:
            count_dict[char] = 0
        else:
            count_dict[char] = count_dict.get(char,0) + 1

    return count_dict





main()