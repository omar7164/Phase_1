#Write one line of Python that takes a given  list a and makes a new list that has only the even elements of this list in it
import random

numlist = []
list_length = random.randint(5, 15)

while len(numlist) < list_length:
    numlist.append(random.randint(1, 75))

evenlist = [number for number in numlist if number % 2 == 0]

print(numlist)
print(evenlist)