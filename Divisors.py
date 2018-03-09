#asks the user for a number and then prints out a list of all the divisors of that number.
__author__ = 'jeffreyhunt'

num = int(input("Please choose a number to divide: "))

listRange = list(range(1,num+1))

divisorList = []

for number in listRange:
    if num % number == 0:
        divisorList.append(number)

print(divisorList)