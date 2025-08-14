def get_book_text(book):
    with open("books/" + book +".txt") as f:
        file_content = f.read()
    return file_content

def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def count_chars(text):
    lower_text = text.lower()
    char_counts = {}
    for char in lower_text:
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1
    return char_counts

def sort_dict(char_dict):
    char_list = []
    for char in char_dict:
        if char.isalpha():
            char_list.append({"char": char, "num": char_dict[char]})
    char_list.sort(key=lambda x: x["num"],reverse=True)
    return char_list