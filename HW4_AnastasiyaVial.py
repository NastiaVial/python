# HW 2 convert to function
#create a list of random number of dicts (from 2 to 10) with random values from 0 to 100 and keys as lowercase letters
from random import randint, choice
from string import ascii_lowercase

def foo(a):
    final_dict = {}
    temp_dict = {}
    for dictionary in a:
        for k, v in dictionary.items():
            temp_dict.setdefault(k, []).append(v)

    print(temp_dict)
#take only the biggest value from temp_dict and rename key with dict number with max value (it`s index value+1)
    for k, v in temp_dict.items():
        if len(v) > 1:
            final_dict[k+"_"+str(v.index(max(v))+1)] = max(v)
        else: final_dict[k] = v[0]
    print(final_dict)

list_of_dicts = [{choice(ascii_lowercase): randint(0, 100)
                      for i in range(len(ascii_lowercase))} for j in range(randint(2, 10))]

foo(list_of_dicts)


# HW 3 convert to function

a = """
tHis iz your homeWork, copy these Text to variable.

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""


def lowercase_with_first_letter_in_uppercace_with_iz_replacement(text):
    lower_text = []
    lower_text = text.lower().replace(' iz ', ' is ')
    str = []
    for i in lower_text.split('.'):
        str.append(i.lstrip().capitalize())
        first_uppercase_letter_in_sentence = ('. '.join(str))
    print(first_uppercase_letter_in_sentence)

lowercase_with_first_letter_in_uppercace_with_iz_replacement(a)
a1 = lowercase_with_first_letter_in_uppercace_with_iz_replacement(a)

def count_whitespaces(text):
    count_whitespaces = 0
# loop for search each index with space or new row
    for i in range(0, len(a)):
        if a[i] == " " or a[i] == "\n":
            count_whitespaces += 1
    print(count_whitespaces)

count_whitespaces(a1)

# # 5. take last word of each sentence and add at the end of the text

def last_word_from_each_sentence_str(text):
    e = []
    for i in text.split('.'):
        if len(i) > 1:
            e.append(i.split()[-1])
        if len(i) == 0:
            i.pop([])
    last_word_str = " ".join(e)
    print(last_word_str)


last_word_from_each_sentence_str(a1)

# add last_word_str into middle of the text a1

# import re
# result = re.search(r"paragraph.", a1)
# print(result.start())

# wrd = 'paragraph.'
# x = a1.split()
# res = x.index(wrd) + 1
# print(res)

# find_index = re.search(r'\b(paragraph)\b', a1)
# print(find_index.start())