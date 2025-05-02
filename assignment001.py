
# numbers = [1, 5, 2, 5, 3, 5, 4]
# filtered_numbers = [num for num in numbers if num != 5]
# print(filtered_numbers)


# my_lst = [1,5,2,5,3,5,4]
# new_list = list(set(my_lst))
# print(new_list)

# def format_string(s):
#     # Remove non-alphabetic characters and spaces
#     s = ''.join(c for c in s if c.isalpha())

#     # Process each character based on its index
#     result = ""
#     index = 0 # To keep track of the position

#     for char in s:
#         if index % 2 == 0:
#             result += char.upper()
#         else:
#             result += char.lower()
#         index += 1
# print(result) 

# import string
# def is_palindrome(text):
#     cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
#     return cleaned_text == cleaned_text[::-1]

# sentences = ["the quick brown dog jumped over the lazy dog", 
#              "madam",
#              "Never odd or Even",
#              "Dennis and Edna sinned",
#              "obi is a boy"]
# for sentence in sentences:
#     print(f'"{sentence}" is a palindrome: {is_palindrome(sentence)}')

# my_var = input('Enter your string: ')
# my_var = my_var.lower().replace(' ','')
# if my_var == my_var[::-1]:
#     print('it is palindrome')
# else: 
#     print('It is not')

# my_tup = (2, 34, 65)
# # print = (type(my_tup))
# # my_tup.

# thistuple = ("Apple",)
# print = (type(thistuple))

# #NOT a tuple
# thistuple = ("Apple")
# print = (type(thistuple))

# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)
# print(x)

# unpacking 
# fruits = ("apple", "banana", "cherry", "strawberry","raspberry")
# (green, yellow,*red) = fruits
# print(green)
# print(yellow)
# print(red)

# fruits = ("apple", "mango", "papaya", "pineapple","cherry")
# (green, *tropic,red) = fruits
# print(green)
# print(tropic)
# print(red)
# thisset = {"apple", "banana", "cherry"}
# tropical = {"orange", "pinapple", "strawberry"}
# thisset.update(tropical)
# print(thisset)
# thisset = {"apple", "banana", "cherry"}
# x = thisset.pop
# print(x)
# print(thisset)

# thisdict = {"brand": "ford","Model": "Mustang", "year": 1964}
# print(len(thisdict))

# thisdict = dict(name = "john", age = 36, country = "Norway")
# print(thisdict)
