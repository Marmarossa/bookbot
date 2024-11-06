def main():
    path = "github.com/Marmarossa/bookbot/books/frankenstein.txt"
    text = get_book_path(path)
    num_words = count_words(text)
    print(count_characters(text))


def count_characters(text):
    lower_text = text.lower()
    char_dict = {}
    for char in lower_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def count_words(text):
    words = text.split()
    return len(words)

def get_book_path(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

main()
