"""
Impractical Python Projects.

Chapter 1
Exercise: Pig Latin
"""

def convert_to_pig_latin(word):
    """
    Convert an english word to Pig Latin.

    Arguments
    ---------
    word: a string with no spaces.

    Description
    -----------
    To form Pig Latin, you take an English word that begins with a consonant,
    move that consonant to the end, and then add “ay” to the end of the word.
    If the word begins with a vowel, you simply add “way” to the end of the
    word.
    """
    list_of_vowels = 'aeiou'

    if word[0] in list_of_vowels:
        word += 'way'
    else:
        word += word[0]+'ay'
        word = word[1:]

    return word

def main():
    """Take a word as input and print in Pig Latin."""
    word = input("Enter a word in English: ")
    print(f"{word} in Pig Latin: {convert_to_pig_latin(word)}")

if __name__ == "__main__":
    main()
