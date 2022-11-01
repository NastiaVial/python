import csv


# 1st part of HW task: word-count (all words are preprocessed in lowercase)
def count_worlds_and_letters() -> object:
    with open("nastia_newsfeed.txt") as f:
        csv_file = f.read()
    # csv_file_lowercase = csv_file.lower()
    words = csv_file.split()
    number_of_words = 0
    words_only = []
    for word in words:
        if word.isalpha():
            number_of_words += 1  # count the number of words
            words_only.append(word)  # create a list with words in lowercase
        else:
            pass

    # take all letters and make two strings with all words from the file (upper and lower cases)
    all_letters = ''.join(words_only)
    all_letters_in_lowercase = all_letters.lower()
    # count the whole number of letters
    qty_of_all_letters = len(all_letters)
    # transfer all words into lowercase mode
    words_only_in_lowercase = [x.lower() for x in words_only]

    # print(words_only)
    # print(words_only_in_lowercase)
    # print(all_letters)
    # print(all_letters_in_lowercase)

    # Iterate over each word in line
    d = dict()
    for word in words_only_in_lowercase:
        # Check if the word is already in dictionary
        if word in d:
            # Increment count of word by 1
            d[word] = d[word] + 1
        else:
            # Add the word to dictionary with count 1
            d[word] = 1

    # print(d)

    with open('words_count.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=':')
        for key in list(d.keys()):
            writer.writerow([key, d[key]])

    # 2nd part of HW task: letter, count_all, count_uppercase, percentage (add header, spacecharacters are not included)
    # count number of letters in the text - use lowercase mode for all letters
    # count number of upper case letters

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    count_all_letters_list = []
    count_upper_letters_list = []
    for letter in alphabet:
        count_all = all_letters_in_lowercase.count(letter)
        count_all_letters_list.append(count_all)
    for letter in alphabet_uppercase:
        count_upper = all_letters.count(letter)
        count_upper_letters_list.append(count_upper)

    # print(count_all_letters_list)
    # print(count_upper_letters_list)
    # print(qty_of_all_letters)

    # for each letter create a list with counts and calculate percentage
    with open('letters_count.csv', 'w', newline='') as csvfile:
        headers = ['letter', 'count_all', 'count_uppercase', 'percentage %']
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        for letter in alphabet:
            index_letter = alphabet.index(letter)
            count_letter = count_all_letters_list[index_letter]
            count_upper_letter = count_upper_letters_list[index_letter]
            count_percent = (int(count_letter) + int(count_upper_letter)) / qty_of_all_letters * 100
            row = [letter, count_letter, count_upper_letter, int(count_percent)]
            writer.writerow(row)

    print(" Letters and words were recounted and saved into two csv files")


# count_worlds_and_letters()