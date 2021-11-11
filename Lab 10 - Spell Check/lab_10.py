import re


# Code to split the text into lines
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


def main():
    # Turning the dictionary into a list
    my_file = open("dictionary.txt")

    dictionary_list = []

    for line in my_file:
        line = line.strip()
        dictionary_list.append(line)

    # Always close the file
    my_file.close()

    # Use the linear search to find words not in dictionary
    print("--- Linear Search ---")

    alice_text = open("AliceInWonderLand200.txt")
    line_number = 0

    # Loop through each line in the alice text
    for line in alice_text:
        word_list = split_line(line)
        line_number += 1

        # Loop through each word in the word list
        for word in word_list:
            position = 0
            while position < len(dictionary_list) and dictionary_list[position] != word.upper():
                position += 1
            if position == len(dictionary_list):
                print("Line", line_number, "possible misspelled word:", word)

    alice_text.close()

    print()
    print("--- Binary Search ---")

    alice_text = open("AliceInWonderLand200.txt")
    line_number = 0

    # Loop through each line in the alice text
    for line in alice_text:
        word_list = split_line(line)
        line_number += 1

        # Loop through each word in the word list
        for word in word_list:
            lower_bound = 0
            upper_bound = len(dictionary_list) - 1
            found = False
            while lower_bound <= upper_bound and not found:
                middle_pos = (lower_bound + upper_bound) // 2
                if dictionary_list[middle_pos] < word.upper():
                    lower_bound = middle_pos + 1
                elif dictionary_list[middle_pos] > word.upper():
                    upper_bound = middle_pos - 1
                else:
                    found = True
            if not found:
                print("Line", line_number, "possible misspelled word:", word)

    alice_text.close()


main()
