from stats import count_words, count_char, dict_sort

#def main():
#    text = get_book_text("books/frankenstein.txt")
#    print(text)

def main():
    num_words = count_words()
    sorted_list_dict = dict_sort()
    #num_char = count_char()
    #print(num_char)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
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