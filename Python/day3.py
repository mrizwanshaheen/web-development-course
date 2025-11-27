# Day 3 - Loops in Python
# Author: Muhammad Rizwan

print("=== FOR LOOP EXAMPLE ===")
for i in range(5):
    print("For loop number:", i)


print("\n=== WHILE LOOP EXAMPLE ===")
count = 1
while count <= 5:
    print("While loop count:", count)
    count += 1


print("\n=== RANGE EXAMPLES ===")
print(list(range(5)))          # 0 to 4
print(list(range(1, 6)))       # 1 to 5
print(list(range(0, 10, 2)))   # Even numbers


print("\n=== BREAK EXAMPLE ===")
for i in range(10):
    if i == 5:
        print("Break at:", i)
        break
    print(i)


print("\n=== CONTINUE EXAMPLE ===")
for i in range(5):
    if i == 2:
        continue      # Skip 2
    print(i)


print("\n=== SHOPPING CART ITERATION ===")
cart = ["Apple", "Milk", "Bread"]
for item in cart:
    print("Item:", item)


print("\n=== SIMPLE LOGIN ATTEMPT (Example Logic) ===")
correct_password = "1234"
attempts = 3

while attempts > 0:
    # password = input("Enter password: ")  # Uncomment if running in real environment
    password = "1234"   # For demo
    if password == correct_password:
        print("Login successful!")
        break
    else:
        attempts -= 1
        print("Wrong password. Attempts left:", attempts)

if attempts == 0:
    print("Account locked!")
