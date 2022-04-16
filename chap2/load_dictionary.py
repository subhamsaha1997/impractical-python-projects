"""This module provides methods to load dictionary and filter one letter words."""
import sys

def load(filename):
    """Load a dictionary text file in a list."""
    try:
        with open(filename, 'r') as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            dictionary_list = [x.lower() for x in loaded_txt]
            return dictionary_list
    except IOError as error:
        print(f"{error}\nError opening {filename}. Terminating Program.", file=sys.stderr)
        sys.exit(1)

def filter_one_letter_word(wordlist):
    """Remove any word which is only has one letter."""
    new_wordlist = [x for x in wordlist if len(x) > 1]
    return new_wordlist

def main():
    """Test the modules above."""
    dictionary_list = load('wordlist.txt')
    # print(dictionary_list[0:10])
    dictionary_without_one_letter_word = filter_one_letter_word(dictionary_list)
    print(dictionary_without_one_letter_word[0:10])

if __name__ == "__main__":
    main()
