def get_letter_count(words):
    lower_text = words.lower()
    num_letters = [x for x in lower_text]
    return num_letters

test = "I love banana"
get_letter_count(test)
num_letter = [x for x in test]
print(num_letter)