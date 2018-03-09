# A program that returns a list that contains only the elements that are common between 2 lists
import random
a = random.sample(range(1,30), 15)  # 15 number of the randam numbers
b = random.sample(range(1,30), 11)
result_overlaps = [i for i in set(a) if i in b]
result = []
for i in result_overlaps:
    if result_overlaps.count(i) == 1:
        result.append(i)
print (result)
