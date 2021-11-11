import re

# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


def main():
    dictionary_list = open("dictionary.txt")

    name_list = []

    for line in dictionary_list:
        line = line.strip()
        name_list.append(line)

    dictionary_list.close()
    print("--- Linear Search ---")

    alice_text = open("AliceInWonderLand200.txt")
    current_line = 0
    word = 0
    for line in alice_text:
        split_line(line)
        word_list = re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)
        line = line.strip()
        for word in word_list:
            while word < len(word_list):
                if dictionary_list != word.upper():
                    print(word)




        # for word in word_list:
        #     if position < len(word_list):
        #         line += word
        #     while current_position < len(word_list):
        #         current_position += 1
        #         if dictionary_list != word.upper():
        #



main()




main()