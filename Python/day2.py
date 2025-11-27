# --------------------------------------------
# DAY 2 – CONDITIONS IN PYTHON
# --------------------------------------------

# 1. Basic If Statement
age = 20
if age >= 18:
    print("You are an adult.")

# 2. If–Else Statement
age = 15
if age >= 18:
    print("Adult")
else:
    print("Minor")

# 3. If–Elif–Else Chain
marks = 75
if marks >= 90:
    print("A Grade")
elif marks >= 80:
    print("B Grade")
elif marks >= 70:
    print("C Grade")
else:
    print("Fail")


# ------------------------------------------------
# Comparison & Logical Operators
# ------------------------------------------------
print("\nComparison Examples:")
print(5 > 3)     # True
print(10 == 7)   # False

print("\nLogical Operator Examples:")
age = 20
if age > 18 and age < 30:
    print("You are a young adult.")

country = "Pakistan"
if country == "Pakistan" or country == "India":
    print("You live in South Asia.")

logged_in = False
if not logged_in:
    print("You are not logged in.")


# ------------------------------------------------
# Nested Conditions
# ------------------------------------------------
age = 20
gender = "male"

if age >= 18:
    if gender == "male":
        print("Adult Male")
    else:
        print("Adult Female")
else:
    print("Not an adult")


# ------------------------------------------------
# Real-Life Example 1: Password Check
# ------------------------------------------------
password = "12345"
# user_input = input("Enter password: ")
# if user_input == password:
#     print("Access Granted")
# else:
#     print("Wrong Password")


# ------------------------------------------------
# Real-Life Example 2: Login System
# ------------------------------------------------
correct_email = "rizwan@example.com"
correct_pass = "1234"

# email = input("Enter email: ")
# pwd = input("Enter password: ")

# if email == correct_email and pwd == correct_pass:
#     print("Login Successful")
# else:
#     print("Invalid credentials")


# ------------------------------------------------
# PRACTICE QUESTIONS (for user to run in Replit)
# ------------------------------------------------

print("\n--- PRACTICE TASKS ---")

# Task 1: Voting Eligibility
# user_age = int(input("Enter your age: "))
# if user_age >= 18:
#     print("Eligible for voting.")
# else:
#     print("Not eligible.")

# Task 2: Number Checker
# num = float(input("Enter a number: "))
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")

# Task 3: Simple Calculator
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# op = input("Enter operation (+, -, *, /): ")

# if op == "+":
#     print("Result:", a + b)
# elif op == "-":
#     print("Result:", a - b)
# elif op == "*":
#     print("Result:", a * b)
# elif op == "/":
#     print("Result:", a / b)
# else:
#     print("Invalid Operation")

# Task 4: Login System (Improved)
# email = input("Enter email: ")
# password = input("Enter password: ")

# if email == correct_email and password == correct_pass:
#     print("Login Successful")
# elif email != correct_email and password != correct_pass:
#     print("Both email and password are incorrect.")
# elif email != correct_email:
#     print("Email is incorrect.")
# else:
#     print("Password is incorrect.")

# Task 5: Discount Program
# price = float(input("Enter price: "))

# if price > 5000:
#     print("You got 20% discount.")
# elif price > 3000:
#     print("You got 15% discount.")
# elif price > 1000:
#     print("You got 10% discount.")
# else:
#     print("No discount.")
