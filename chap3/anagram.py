import sys
sys.path.insert(0, "../chap2/")

import load_dictionary as ld

def find_anagram_word(query_word):
    """Find anagram of an input word."""
    sorted_query_word = sorted(query_word) 
    word_list = ld.filter_one_letter_word(ld.load("../chap2/wordlist.txt"))
    print(f"Loaded dictionary with {len(word_list)} words.")
    list_of_anagrams = []

    for word in word_list:
        word = word.lower()
        if (sorted_query_word == sorted(word)) and (query_word != word):
            list_of_anagrams.append(word)

    return list_of_anagrams

def main():
    in_word = input("Please input the word to find anagram: ")
    in_word = in_word.lower()
    print(f"Finding anagram for {in_word} instead.")

    anagram = find_anagram_word(in_word)
    if len(anagram) == 0:
        print("We need a bigger dictionary.")
    else:
        print("And the anagrams are: ", *anagram)

if __name__ == "__main__":
    main()

