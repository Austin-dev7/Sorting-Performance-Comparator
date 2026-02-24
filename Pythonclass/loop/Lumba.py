# def get_highest(numbers):
#     highes = numbers [0]
#     for num in numbers:
#         if num >highes:
#             highes=num
#     return highes
# num=[3,10,6,21,5]
# print(get_highest(num) )

# def get_highest(numbers):
#     highest=numbers[0]
#     for num in numbers:
#         if num >highest:
#             highest=num
#     return highest
# num=[22,30,44,50]
# print (get_highest(num))

# def get_highest(numbers):
#     highest=numbers[0]
#     for num in numbers:
#         if num > highest:
#          highest = num
#     return highest
# num=[10,15,30,14]
# print(get_highest(num))

# def get_lowest(numbers):
#     lowest=numbers[0]
#     for num in numbers:
#         if num <lowest:
#             lowest=num
#     return lowest
# num=[9,4,6,12]
# 0,print(get_lowest(num))
#

# # def mul(a,d):
#     mul = a*d
#     return mul
# a=mul(2,3)
# print(a)

# lambda argument: expression
# add = lambda a,b: a+b
# print(add(2,2)
#

# add = lambda a,b: a * b
# print(add(5,2))

# lambda argument: expression

# age = int(input("Enter your age: "))
# if age >= 18: print("you are eligible for admission")


# is_even = lambda x: x % 2 == 0
# is_even = lambda x: x % 2 == 0
#
# age_check = lambda age: "An Adult" if age >=18 else "a minor"
# print(age_check(15))

# lambda  age: "An adult" if age >=18 else "a minor"
# age_check = lambda age:"An Andult" if age >=18 else "a minor"
# print(f"your age {age_check(23)}")
# good = lambda a,b :a + b
# print({good( 2, 2,)})
# #

# people = [
#     {"name": "John", "age": 30},
#     {"name": "Alice", "age": 25},
#     {"name": "Bob", "age": 40},
#     {"name": "Eve", "age": 20},
#     {"name": "Mike", "age": 35}]
# people_sorted = sorted(people, key=lambda g: g['age'])
# print(people_sorted)

# import os
#
# folder = "image"
# files = os.listdir(folder)
#
# for i,in enumerate(files,start=1):
#     ext = os.path.splitext(file)[1]
#     new_name = f"image_{i}{ext}"
#     os.rename(os.path.join(folder, file), os.path.join(folder,new_name))


# time = open("aug.py",'w')
# time.write("good girl")

# ht = ("thought")
# print(ht)