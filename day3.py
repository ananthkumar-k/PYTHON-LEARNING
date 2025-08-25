# # Q1
# def greet():
#     print("Hello, Welcome to Python!")

# greet()
# greet()
# greet()

# # Q2
# def add_numbers(a, b):
#     return a + b

# print(add_numbers(5, 7))

# # Q3
# def power(base, exponent=2):
#     return base ** exponent

# print(power(5))

# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False

# print(is_even(4))
# print(is_even(7))

# # Q5
# def find_max(lst):
#     return max(lst)

# print(find_max([10, 50, 30, 20]))

# # Q6
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(5))

# # Q7
# def total_sum(*numbers):
#     return sum(numbers)

# print(total_sum(10, 20, 30))

# # Q8
# def student_details(**info):
#     for key, value in info.items():
#         print(key, ":", value)

# student_details(name="Sam", age=20, course="Python")

# # Q9
# def outer():
#     def inner():
#         print("Inner Function Called")
#     inner()

# outer()

# # Q10
# def count_vowels(text):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for ch in text:
#         if ch in vowels:
#             count += 1
#     return count

# print(count_vowels("hello world"))

