a = """
tHis iz your homeWork, copy these Text to variable.

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""


# 1. make all letters in lowercase
a.lower()
b = a.lower()

# 2. replace iz for is
c = b.replace(' iz ', ' is ')
# print(c)

# 3. start each sentance  with Uppercase letter
str = []
for i in c.split('.'):
    str.append(i.lstrip().capitalize())
    d = ('. '.join(str))
print(d)


import re
# print(len(re.findall(" ", a)))
# print(len(re.findall("\n", a)))

# 4. count whitespaces
count_whitespaces = 0
# loop for search each index with space or new row
for i in range(0, len(a)):
    if a[i] == " " or a[i] == "\n":
        count_whitespaces += 1
print(count_whitespaces)

# 5. take last word of each sentence and add at the end of the text
# in order to take last word of each sentence i did following:
#  divide all text for sentences using "."
# e = []
# for i in d.split('.'):
#     print(i)
#     if len(i) > 1:
#         e.append(i.split()[-1])
#     if len(i) == 0:
#         i.pop([])
# print(e)
#
# # convert list to string
# last_word_str = " ".join(e)
# print(last_word_str)


# function

def last_word_from_each_sentence_str(text):
    e = []
    for i in text.split('.'):
        if len(i) > 1:
            e.append(i.split()[-1])
        if len(i) == 0:
            i.pop([])
    last_word_str = " ".join(e)
    print(last_word_str)


last_word_from_each_sentence_str(d)