def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    print(f"There are {num_words} words in this text")
    num_letters = get_letter_count(text)
    
    print()
    for item in num_letters:
        print(f"The {item['letter']} character was found {item['num']} times")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_word_count(text):
    words = text.split()
    return len(words)

def sort_on(dict):
    return dict["num"]

def get_letter_count(text):
    dict_letters = {}
    lower_text= text.lower()
    for letter in lower_text:
        if letter.isalpha() == True:
            if letter in dict_letters:
                dict_letters[letter] += 1
            else:
                dict_letters[letter] = 1

    order_dict = []
    for lt in dict_letters:
        order_dict.append({"letter": lt, "num":dict_letters[lt]})
    order_dict.sort(reverse=True, key = sort_on)
    
    return order_dict
        

main()