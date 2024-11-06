def main():
    with open("github.com/Marmarossa/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()

    def count_words():
        
        words = file_contents.split()
        return len(words)

    print(count_words())
main()
