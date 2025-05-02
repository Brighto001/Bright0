# def fibonacci(n):
#     fib_sequence = [0, 1]
#     for i in range(2, n):
#         fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
#         return fib_sequence[:n]

# # Example: Get the first 10 Fibonacci numbers
# n = int(input("Enter the number of Fibonacci terms:"))
# print(fibonacci(n))

# def factorial(n):
#     if n== 0 or n == 1:
#         return 1
#     return n * factorial(n-1)

# # Example: Get factorial of a number
# num = int(input("Enter a number: "))
# print(f"factorial of {num} is{factorial(num)}")

# def fact(n):
#     f = 1
#     for i in range(1, n+1):
#         f*=i
#     return f

# x = 6
# result = fact(x)
# print(result)

# def fact(n):
#     if n < 0:
#         return f"Undefined Result"
#     elif n ==0 or n == 1:
#         return 1
    
#     else: 
#         return n * fact(n-1)
    
# def fib(n):
#     a = 0
#     b =1
#     if n<= 0:
#         return []
    
#     elif n == 1:
#         return a
#     else:
#         my_fibseqq = [a, b] 
#         for i in renge(2,n):


# def my_function(food):
#     for x in food:
#         print(x)
# fruits = ["apple", "banana", "cherry"]
# my_function(fruits)

# x = lambda a : a + 10
# print(x(5))

# def myfunc(n):
#     return lambda a : a * n
# mydoubler = myfunc(2)
# print(mydoubler(11))

# import matplotlib.pyplot as plt

# # Data
# x = [1,2,3,4,5]
# y = [2,4,6,8,10]

# # Create a figure
# plt.figure(figsize=(8, 6), dpi=100)

# # Add a line plot to the figure
# plt.plot(x, y, label='Line Plot')

# # Customize the plot
# plt.title('Figure with line plot')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.legend()

# # Display the figure

# plt.show()

# import matplotlib.pyplot as plt
# # Using a specific style
# plt.style.use('seaborn-v0_8-bright')

# # Creating a sample plot
# plt.plot([1, 2, 3, 4,], [10, 15, 25, 30])
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('sample plot')
# plt.show

# import matplotlib.pyplot as plt
# print(plt.style.available) # Print availabble style

# import matplotlib.pyplot as plt
# x = [1, 2, 3]
# y1 = [2, 4, 6]
# y2 = [1, 3, 5]
# y3 = [3, 6, 9]

# #Plotting the data 
# line1, = plt.plot(x, y1)
# line2, = plt.plot(x, y2)
# line3, = plt.plot(x, y3)

# # Calling legend with explicitly listed artists and labels
# plt.legend([line1, line2, line3], ['label 1', 'label 2', 'label 3'])

# # Show the plot 
# plt.show()
# print('Successfully placed a legend on the axes...')

# import matplotlib.pyplot  as plt

# x = [1, 2, 3, 4, 5]
# y1 = [10, 15, 7, 12, 8]
# y2 = [8, 12, 6, 10, 15]


# plt.plot(x, y1, label='Line 1')
# plt.plot(x, y2, label='Line 2', linestyle='--', marker='o')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Multiple lines with Legend')
# plt.legend()
# plt.show()


import matplotlib.pyplot  as plt
categories = ['Category A', 'Category B', 'Category C']
values = [15, 24, 30]

plt.bar(categories, values, color= 'Orange')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Basic Vertical Bar Graph')
plt.show()