#!/usr/bin/python3


import sys
import os
from stats import get_word_count
from stats import get_char_dict
from textwrap import dedent



def main(file_path):

    full_book_text = get_book_text(file_path)
    num_words = get_word_count(full_book_text)
    character_dictionary = get_char_dict(full_book_text)


    report_head = dedent(f"""
        ============ BOOKBOT ============
        Analyzing book found at {file_path}...
        ----------- Word Count ----------
        Found {num_words} total words
        -------- Character Count --------""")
    print(report_head)

    for key, value in character_dictionary.items():
        if key == "\n":
            print_key = "enter"
            print(f"{print_key}: {value}")
        elif key == " ":
            print_key = "space"
            print(f"{print_key}: {value}")
        elif key == "\t":
            print_key = "tab"
            print(f"{print_key}: {value}")
        else:
            print(f"{key}: {value}")

    report_foot = "============== END =============="
    print(report_foot)

def get_book_text(file_path):

    with open(file_path) as f:
        book_text = f.read()

    return book_text


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        selected_path = sys.argv[1]
        if not os.path.isfile(selected_path):
            print(f"The file '{selected_path}' does not exist or is not a valid file path. Please check the path and try again")
            sys.exit(1)
        main(selected_path)

