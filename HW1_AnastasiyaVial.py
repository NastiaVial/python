import random
#  use random.sample() to create range of 100 numbers from 0 to 1000
randomlist = random.sample(range(0,1000), 100)
print(randomlist)

# use range(len(someList)) with a for loop to iterate over the indexes of a list.
# Code in the loop can access the index (as the variable i) and the value at that index (as randomlist[i])

for i in range(len (randomlist)):
    for j in range(i+1, len(randomlist)):
        # compare two values and swap them if needed
        if randomlist[i] > randomlist[j]:
            randomlist[i], randomlist[j] = randomlist[j], randomlist[i]
            print(randomlist)

# sort all numbers for odd and even using %2 . then print average values for each list of values
def average_odd_and_numbers(randomlist):
    even_numbers = []
    odd_numbers = []
    for number in randomlist:
        if number % 2 == 0:
            even_numbers.append(number)
        if number % 2 != 0:
            odd_numbers.append(number)

    print("average even numbers = ", sum(even_numbers) / len(even_numbers))
    print("average odd numbers = ", sum(odd_numbers) / len(odd_numbers))


average_odd_and_numbers(randomlist)