# HW 2 convert to function
#create a list of random number of dicts (from 2 to 10) with random values from 0 to 100 and keys as lowercase letters
from random import randint, choice
from string import ascii_lowercase


#function to create random list of dictionaries
def create_random_list_of_dicts():
    list_of_dicts = []
    list_of_dicts = [{choice(ascii_lowercase): randint(0, 100)
                      for i in range(len(ascii_lowercase))} for j in range(randint(2, 10))]
    return list_of_dicts


random_list = create_random_list_of_dicts()
print(random_list)


#function that takes all keys from list of dictionaries and create one with whole values for each key with default -1
# for those values that where absent in any of presented dictionaries in list
def list_of_whole_keys_and_values(list_of_dicts):
    temp_dict = {}
    keys = set().union(*list_of_dicts)
    for dictionary in list_of_dicts:
        for k in keys:
            #use get(key) and add default value instead of None
            temp_dict.setdefault(k, []).append(dictionary.get(k, -1))
    #use print just to show the result for this exercize
    return temp_dict
#take only the biggest value from temp_dict and rename key with dict number with max value (it`s index value+1)


union_dictionary = list_of_whole_keys_and_values(random_list)
print(union_dictionary)


# function that takes only highest values for each key
def dict_with_highest_values(some_dict):
    final_dict = {}
    for k, v in some_dict.items():
        final_dict[k + "_" + str(v.index(max(v)) + 1)] = max(v)
    return final_dict

print(dict_with_highest_values(union_dictionary))

