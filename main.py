from stats import count_words

#def main():
#    text = get_book_text("books/frankenstein.txt")
#    print(text)

def main():
    num_words = count_words()
    print(f"Found {num_words} total words")

main()