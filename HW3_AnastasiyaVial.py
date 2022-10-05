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
e = []

for i in d.split('.'):
    for j in i.split():
        e.append(i.split()[-1])
print(e)

# for i in d.split('.'):
#     e.append(i.split())
# # print(e)
#
# #save each sentence into variable
# e1=e[0]
# e2=e[1]
# e3=e[2]
# e4=e[3]
# e5=e[4]
# e6=e[5]
# e7=e[6]
# e8=e[7]
#
# #create variable and add all last words from each sentence
# last_word_of_each_sentence_at_the_end = d + " " +e1[-1] + " " +e2[-1] + " " +e3[-1]+ " " +e4[-1]+ " " +e5[-1]+ " " +e6[-1]+ " " +e7[-1]+ " " +e8[-1]
# print(last_word_of_each_sentence_at_the_end)


# i tried to do in some other way
# unfortunately it doesn`t work

# last_word_from_each_sent= []
# for i in d.split('.'):
#     last_word_from_each_sent.append.i.split()[-1]
# print(last_word_from_each_sent)
