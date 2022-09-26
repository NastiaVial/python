
#create a list of random number of dicts (from 2 to 10) with random values from 0 to 100 and keys as lowercase letters
from random import randint, choice
from string import ascii_lowercase
list_of_dicts = [{choice(ascii_lowercase): randint(0, 100)
                  for i in range(len(ascii_lowercase))} for j in range(randint(2, 10))]
print(list_of_dicts)

#create empty dictionaries. one for temporary usage and ond for final results
final_dict = {}
temp_dict = {}

#convert list of dicts into dict of lists.
# each key from temp_dict will contain all values from list_of_dicts

for dictionary in list_of_dicts:
  for k, v in dictionary.items():
    temp_dict.setdefault(k, []).append(v)
print(temp_dict)

#take only the biggest value from temp_dict and rename key with dict number with max value (it`s index value+1)
for k, v in temp_dict.items():
  if len(v) > 1:
    final_dict[k+"_"+str(v.index(max(v))+1)] = max(v)
  else: final_dict[k] = v[0]

print(final_dict)