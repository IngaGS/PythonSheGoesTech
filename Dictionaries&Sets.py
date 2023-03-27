# TASK 1:

# def Sum():
#     a = input("Enter the first number: ")
#     b = input("Enter the second number: ")
#     return int(a) + int(b)
# result = Sum()
# print("The sum is:", result)

# TASK2

# def count_vowels(user_input):
#     vowels = "aeiou"
#     count = 0
#     for char in user_input:
#         if char in vowels:
#             count += 1
#     return count
#
# user_input = input("Enter a string: ")
# num_vowels = count_vowels(user_input)
# print("The number of vowels in the string is:", num_vowels)

#TASK 3

# def Pal(text):
#     return text == text[::-1]
#
# text=input("Enter a text: ")
#
# print ("The text is a palindrome: ", Pal(text))

# TASK 4
# Write a function that takes a list of integers as a parameter and returns a list of only the even
# integers in the original list

# my_list=[1,3,6,4,7,8,22,6,33,97,51,44]
# def even(list):
#     list_even = []
#     for number in list:
#         if number % 2 == 0:
#             list_even.append(number)
#     return list_even
#
# print (even(my_list))


# TASK 5:
# Write a function that takes a list of integers and a target sum as parameters and returns
# a list of two integers from the original list that add up to the target sum.

# my_list=[1,2,3,4,5,7,8,18,23,6,9,27,44]
#
# def my_sum(my_list, target_sum):
#     for i in range(len(my_list)):
#         for j in range(i + 1, len(my_list)):
#             sum_values = my_list[i] + my_list[j]
#             if sum_values == target_sum:
#                 return [my_list[i], my_list[j]]
#     return []
#
# target_sum=int(input("Enter the target sum\n"))
# result = my_sum(my_list, target_sum)
# if result:
#     print(f'Target sum {target_sum} is a sum of these two integers from the list {result}')
# else:
#     print(f'Target sum {target_sum} cannot be achieved from the list')


#Task 6: Write a function that takes a list of integers as a parameter and returns
#the product of all the integers in the list.

# my_list=[1,2,3,4,5,7,8,18,23,6,9,27,44]
#
# def Multi(my_list):
#     result=1
#     for i in my_list:
#         result=result*i
#     return result
#
# print (Multi(my_list))

# Task 8:Write a function that takes a dictionary as a parameter and returns a list
# of all the keys in the dictionary that have an even value

# my_dict= { "grass":1, "leaves":2, "trees":3, "sand":4, "flower":5, "river":6}
#
# def even_value(my_dict):
#     my_dict2=[]
#     for key in my_dict.key():
#         if my_dict[key] % 2 ==0:
#            my_dict2.append(key)
#     return my_dict2
#
# print(even_value(my_dict))

# Task 9:Write a function that takes a list of dictionaries as a parameter and returns a new
# dictionary that contains the sum of the values for each key in the original dictionaries.

# my_dict=[
#     {'a': 12, 'b':43, 'c':3, 'd':17 },
#     {'a': 4, 'b':22, 'c':8, 'd':1 },
#     {'a': 7, 'b':52, 'c':4, 'd':31 }
# ]
# new_dict={}
# def sum_dict(my_dict):
#     for i in my_dict:
#         for k in i.keys():
#             new_dict[k] = new_dict.get(k, 0) + i[k]
#     return (new_dict)
#
# print (sum_dict(my_dict))

# Task 10:Write a function that takes a tuple as a parameter and returns
# a new tuple that has the first and last elements swapped.

# my_tuple = ("green", "blue", "yellow", "orange")
#
# list_my_tuple=list(my_tuple)
#
# list_my_tuple[0], list_my_tuple[-1]=list_my_tuple[-1], list_my_tuple[0]
# new_tuple=tuple(list_my_tuple)
# print(new_tuple)

# Task 11:Write a function that takes a set as a parameter and returns a new set
# that contains only the elements that are not divisible by 3.
# my_set={1,2,3,4,5,7,8,18,23,6,9,27,44}
# new_set= {}
#
# def divide3(my_set):
#     new_set=set()
#     for i in my_set:
#         if i%3 !=0:
#             new_set.add(i)
#     return(new_set)
#
# print (divide3(my_set))












