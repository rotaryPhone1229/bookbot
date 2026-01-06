from stats import count_words, count_char, dict_sort
import sys

#def main():
#    text = get_book_text("books/frankenstein.txt")
#    print(text)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    num_words = count_words()
    sorted_list_dict = dict_sort()
    #num_char = count_char()
    #print(num_char)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    #print(sorted_list_dict)
    for item in sorted_list_dict:
        if not (item["char"].isalpha()) or (item["char"] == 'OTHER'):
            continue
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")


main()