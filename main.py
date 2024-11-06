def main():
    path = "github.com/Marmarossa/bookbot/books/frankenstein.txt"
    print_report(path)
def print_report(path):
    text = get_book_path(path)
    num_words = count_words(text)
    char_dict = count_characters(text)
    char_sorted_list = chars_dict_to_sorted_list(char_dict)
    print(f"---Begin report for {path}---")
    print(f"{num_words} words found in the document")
    for item in char_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The {item['char']} character was found {item['num']} times")
    print("---End report---")


def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(nums_char_dict):
    sorted_list =[]
    for ch in nums_char_dict:
        sorted_list.append({"char": ch, "num": nums_char_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

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
