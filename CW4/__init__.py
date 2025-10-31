# from pprint import pprint
#
# dic = {
#     "Ebrahim": {
#         "name": "Ebrahim",
#         "age": 32,
#         "city": "Tehtran",
#         "email": "Ebrahim@mail.com",
#     },
#     "Ali": {
#         "name": "Ali",
#         "age": 30,
#         "city": "Shiraz",
#         "email": "Ali@mail.com",
#     }
# }
#
# name = input("enter your name: ")
# # name = "Ebrahim"
# if name in dic:
#     pprint(dic[name])
# else:
#     pprint("name is not exist.")
#
# --------------------------------
#
#
# def calculate(user_number):
#     if user_number < 0: return "Not valid"
#
#     result = sum(number for number in range(user_number + 1) if number % 2 == 0)
#     # for number in range(user_number + 1):
#     #     if number % 2 == 0:
#     #         result += number
#
#     return result
#
#
# user_input = int(input("Please enter a number: "))
# print(calculate(user_input))
#
# --------------------------------
#
# n = int(input("Enter a number : "))
# for i in range(n, 0, -1):
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print()
#
# ----------------------------------
#
# with open('notes.txt', 'a') as f:
#     user_input = input('enter:(for exit 0) ')
#
#     while user_input != '0':
#         f.write(user_input + '\n')
#         user_input = input('enter:(for exit 0)')
#
# ---------------------------------
# ​from pprint import pprint
#
# dic = {
#     "Ebrahim": {
#         "name": "Ebrahim",
#         "age": 32,
#         "city": "Tehtran",
#         "email": "Ebrahim@mail.com",
#     },
#     "Ali": {
#         "name": "Ali",
#         "age": 30,
#         "city": "Shiraz",
#         "email": "Ali@mail.com",
#     }
# }
#
# name = input("enter your name: ")
# # name = "Ebrahim"
# if name in dic:
#     pprint(dic[name])
# else:
#     pprint("name is not exist.")
#
# --------------------------------
#
#
# def calculate(user_number):
#     if user_number < 0: return "Not valid"
#
#     result = sum(number for number in range(user_number + 1) if number % 2 == 0)
#     # for number in range(user_number + 1):
#     #     if number % 2 == 0:
#     #         result += number
#
#     return result
#
#
# user_input = int(input("Please enter a number: "))
# print(calculate(user_input))
#
# --------------------------------
#
# n = int(input("Enter a number : "))
# for i in range(n, 0, -1):
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print()
#
# ----------------------------------
#
# with open('notes.txt', 'a') as f:
#     user_input = input('enter:(for exit 0) ')
#
#     while user_input != '0':
#         f.write(user_input + '\n')
#         user_input = input('enter:(for exit 0)')
#
# try:
#     with open("note.txt") as file:
#         lines = file.readlines()
#
#         num_lines = len(lines)
#         num_chars = sum(len(line) for line in lines)
#         num_words = sum(len(line.split(" ")) for line in lines)
#
#         print("lines:", num_lines)
#         print("words:", num_words)
#         print("characters:", num_chars)
#
# except FileNotFoundError:
#     print("File not found")
#
#
#
