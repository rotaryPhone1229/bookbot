def get_book_text(file_path):
    #Returns the text as a string
    with open(file_path) as f:
        return f.read()

def count_words():
    #Splits the string so each word is item in list, counts words
    words = get_book_text("books/frankenstein.txt").split()
    num_words = len(words)
    return num_words

def count_char():
    char_dict = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 
                 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0,
                 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0,
                 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0,
                 'y':0, 'z':0, ' ':0, ',':0, '.':0, '!':0,
                 '/':0, '"':0, '1':0, '2':0, '3':0, '4':0,
                 '5':0, '6':0, '7':0, '8':0, '9':0, '0':0,
                 'æ':0, 'â':0, 'ê':0, 'ë':0, 'ô':0, 'OTHER': 0}
    chars = get_book_text("books/frankenstein.txt").lower()
    for i in chars:
        if i in char_dict:
            char_dict[i] += 1
        else:
            char_dict['OTHER'] += 1
    return char_dict

def sort_on(item):
    return item["num"]

def dict_sort():
    list_o_dicts = []
    num_chars = count_char()
    for item in num_chars:
        list_o_dicts.append({"char":item, "num":num_chars[item]})
    list_o_dicts.sort(reverse=True, key=sort_on)
    return list_o_dicts
    
