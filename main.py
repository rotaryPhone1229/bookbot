from stats import count_words, count_char

#def main():
#    text = get_book_text("books/frankenstein.txt")
#    print(text)

def main():
    num_words = count_words()
    print(f"Found {num_words} total words")
    num_char = count_char()
    print(num_char)

main()