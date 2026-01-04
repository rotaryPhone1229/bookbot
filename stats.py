def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def count_words():
    words = get_book_text("books/frankenstein.txt").split()
    num_words = len(words)
    return num_words