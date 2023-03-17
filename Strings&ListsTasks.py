# TASK 1

import re
# sentence = input("Enter a sentence: \n")
# letter = input("Enter a letter: \n")
#print("There are " + str(sentence.count(letter)) + " letters " + letter + " in your sentence")

# TASK 1.1.
# sentence = input("Enter a sentence: \n")
# lenght= sentence.__len__()
#
# i=0
# while i<(lenght):
#     letter = sentence[i]
#     count=sentence.count(letter)
#     i += 1
#     print("There are " + str(count) + " letters " + letter + " in your sentence")
#
# # question1: how to print a letter and it's count only once?

# TASK 2:
list=["sun", "clouds", "rain", "snow", "grass", "trees", "flowers", "river", "sea", "leaves", "spring", "summer", "winter", "autumn"]
# list.sort()
# print(list)

list_sorted=[]
while list:
    minvalue = min(list)
    list_sorted.append(minvalue)
    list.remove(minvalue)

print(list_sorted)



