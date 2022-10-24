import csv
# 1st part of HW task: word-count (all words are preprocessed in lowercase)
# create two strings with letters only: one in lowercase (here in 1st part of task)  and second with the same letters as per txt file (second part of task)
# read file then lowercase all text and split by words
with open("nastia_newsfeed.txt") as f:
    csv_file = f.read()
csv_file_lowercase = csv_file.lower()
words = csv_file_lowercase.split()
number_of_words = 0
lowercase_words_only = []
for word in words:
    if word.isalpha():
        number_of_words += 1     # count the number of words
        lowercase_words_only.append(word)   # create a list with words in lowercase
    else:
        pass

# take all letters and make string with all words from the file
all_letters_in_lowercase = ''.join(lowercase_words_only)

# print(lowercase_words_only)
# print(number_of_words)
# print(all_letters_in_lowercase)

# create a csv, write the number of words to csv with delimiter ':'
# words : number_of_words
with open('words_count.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=':')
    writer.writerow(['words', str(number_of_words)])


# 2nd part of HW task: letter, count_all, count_uppercase, percentage (add header, spacecharacters are not included)
# create string with the same letters as per txt file
with open("nastia_newsfeed.txt") as f:
    csv_file = f.read()
words = csv_file.split()
all_words_only = []
for word in words:
    if word.isalpha():
        all_words_only.append(word)
    else:
        pass

# take all letters and make string with all words from the file (upper and lower cases)
all_letters_only = ''.join(all_words_only)

# count the whole number of letters
qty_of_all_letters = len(all_letters_only)

# print(all_words_only)
# print(all_letters_only)
# print(qty_of_all_letters)


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
    count_upper = all_letters_only.count(letter)
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