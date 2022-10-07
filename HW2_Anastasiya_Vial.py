
#create a list of random number of dicts (from 2 to 10) with random values from 0 to 100 and keys as lowercase letters
from random import randint, choice
from string import ascii_lowercase
list_of_dicts = [{choice(ascii_lowercase): randint(0, 100)
                  for i in range(len(ascii_lowercase))} for j in range(randint(2, 10))]
print(list_of_dicts)

#create empty dictionaries. one for temporary usage and ond for final results
final_dict = {}
temp_dict = {}

for dictionary in list_of_dicts:
    for k, v in dictionary.items():
        if k not in dictionary:
            temp_dict.setdefault(k, []).append(v(None))
        if k in dictionary:
            temp_dict.setdefault(k, []).append(v)

print(temp_dict)


#tried this option as well
from collections import defaultdict
d = defaultdict(list)
for dictionary in list_of_dicts:
    for k, v in dictionary.items():
#         try:
#         if k[0] not in k[1]:
#             d[k].append(v(None))
#         if k[1] not in k[2]:
#             d[k].append(v(None))
#         if k[2] not in k[3]:
#             d[k].append(v(None))
#         if k[3] not in k[4]:
#             d[k].append(v(None))
#         if k[4] not in k[5]:
#             d[k].append(v(None))
#         if k[5] not in k[6]:
#             d[k].append(v(None))
#         if k[6] not in k[7]:
#             d[k].append(v(None))
#         if k[7] not in k[8]:
#             d[k].append(v(None))
#         if k[8] not in k[9]:
#                 d[k].append(v(None))
#         else:
#             d[k].append(v)
#
# print(d)





#convert list of dicts into dict of lists.
# each key from temp_dict will contain all values from list_of_dicts

# for dictionary in list_of_dicts:
#   for k, v in dictionary.items():
#     temp_dict.setdefault(k, []).append(v)
# print(temp_dict)

#take only the biggest value from temp_dict and rename key with dict number with max value (it`s index value+1)
for k, v in temp_dict.items():
  if len(v) > 1:
    final_dict[k+"_"+str(v.index(max(v))+1)] = max(v)
  else: final_dict[k] = v[0]

print(final_dict)