# HW 3 convert to function
import re

a = """
tHis iz your homeWork, copy these Text to variable.

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""


def lowercase_with_first_letter_in_uppercace(text):
    lower_text = []
    lower_text = text.lower()
    str_ap = []
    for i in lower_text.split('.'):
        str_ap.append(i.lstrip().capitalize())
    first_uppercase_letter_in_sentence = ('. '.join(str_ap))
    return first_uppercase_letter_in_sentence


text_in_lowercase = lowercase_with_first_letter_in_uppercace(a)
# print(text_in_lowercase)


def replace_iz_is(text_in_lowercase):
    updated_text = []
    updated_text = text_in_lowercase.replace(' iz ', ' is ')
    return updated_text


corrected_text = replace_iz_is(text_in_lowercase)
# print(corrected_text)


def count_whitespaces(text):
    whitespaces_qty = 0
# loop for search each index with space or new row
    for i in range(0, len(text)):
        if text[i] == " " or text[i] == "\n":
            whitespaces_qty += 1
    return whitespaces_qty


qty_of_whitespaces_in_text = count_whitespaces(corrected_text)
# print(qty_of_whitespaces_in_text)

# # 5. take last word of each sentence and add after the "paragraph."

def last_word_from_each_sentence_str(text):
    e = []
    for i in text.split('.'):
        if len(i) > 1:
            e.append(i.split()[-1])
        if len(i) == 0:
            i.pop([])
    last_word_str = " ".join(e)
    return last_word_str


last_word = last_word_from_each_sentence_str(corrected_text)
# print(last_word)




def insert_words_inside(words_to_find,words_to_add):
    # searching the index for "paragraph."
    index_number = re.search(words_to_find, corrected_text).end()
    result = corrected_text[:index_number+1] + words_to_add.capitalize()
    return result


word = r"paragraph."
# print(insert_words_inside(word, last_word))