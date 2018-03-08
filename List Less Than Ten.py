# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
num = int(input("Choose a number: "))
new_list = []
for i in a:
	if i < num:
		new_list.append(i)
print (new_list)