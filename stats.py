#!/usr/bin/python3


def get_word_count(book_text):

    word_list = book_text.split()
    word_count = len(word_list)

    return word_count


def get_char_dict(book_text):

    char_dict = {}
    lower_book_text = book_text.lower()

    for character in lower_book_text:
        if character in char_dict:
            char_dict[character] += 1
        else:
            char_dict[character] = 1
  
    sorted_list = sorted(char_dict.items(), key=lambda item: item[1], reverse = True)
    sorted_char_dict = dict(sorted_list)

    return sorted_char_dict