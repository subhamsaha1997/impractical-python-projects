"""
Impractical Python Projects.

Chapter 1
Poor Man's Bar Chart
"""

def freq_of_letters(sentence):
    """Make dictionary with frequency of letters in sentence."""
    freq_dict = {} # initialize with an empty dictionary
    sentence = sentence.lower() # make all letters lowercase
    for letter in sentence:
        if letter.isalpha():
            if letter in freq_dict:
                freq_dict[letter] += 1
            else:
                freq_dict[letter] = 1

    return freq_dict

def draw_col(tag, freq):
    """Draw a bar with tag and frequency."""
    print(tag, end=" ")
    print("|", end=" ")
    for _ in range(freq):
        print("*", end="")

def draw_chart(freq_dict):
    """Draw bar chart from a frequency dictionary."""
    for k in freq_dict:
        draw_col(k, freq_dict[k])
        print()

def main():
    """Take input a sentence and draw bar chart with frequency of letters."""
    sentence = input("Text: ")
    draw_chart(freq_of_letters(sentence))



if __name__ == "__main__":
    main()
