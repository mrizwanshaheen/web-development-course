# Day 1 – Python Basics Practice

# Printing a welcome message
print("Welcome to Day 1 of Python Learning!")

# Variables and Data Types
name = "Rizwan"
age = 26
height = 5.9
is_student = True

print("\n--- Variables ---")
print(name, age, height, is_student)

# Type checking
print("\n--- Data Types ---")
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

# Type Conversion
age_str = str(age)
num_from_string = int("45")
decimal_from_string = float("3.14")

print("\n--- Type Conversion ---")
print("Age as string:", age_str)
print("Integer from '45':", num_from_string)
print("Float from '3.14':", decimal_from_string)

# User Input
print("\n--- User Input Example ---")
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

print(f"Hello {user_name}, you are {user_age} years old!")

# Math Operations
print("\n--- Math Operations ---")
a = 10
b = 3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Remainder:", a % b)
print("Power:", a ** b)
