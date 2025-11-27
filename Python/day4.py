# Day 4 - Lists & Tuples Practice
# Just practicing some basics of Python data structures

# --- LIST PRACTICE ---

# Creating a simple list of fruits
fruits = ["apple", "banana", "mango"]
print("Starting fruits:", fruits)

# Accessing values by index
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Updating a value (lists are changeable)
fruits[1] = "orange"
print("After update:", fruits)

# Adding new items
fruits.append("grapes")      # adds at the end
fruits.insert(1, "kiwi")     # inserts at index 1
print("After adding items:", fruits)

# Removing values
fruits.remove("apple")       # removes by name
last_item = fruits.pop()     # removes last item
print("Removed:", last_item)
print("After removing:", fruits)

# Total items
print("Total fruits now:", len(fruits))

# Looping through list
print("\nLooping through fruit list:")
for item in fruits:
    print(item)



# --- LIST SLICING ---

numbers = [10, 20, 30, 40, 50]
print("\nNumbers list:", numbers)

# Different slicing examples
print("numbers[1:4] →", numbers[1:4])
print("numbers[:3]  →", numbers[:3])
print("numbers[2:]  →", numbers[2:])
print("numbers[0:5:2] →", numbers[0:5:2])  # skipping by 2



# --- TUPLE PRACTICE ---

# Tuple example (unchangeable list)
person = ("Rizwan", 26, "Pakistan")
print("\nPerson tuple:", person)

# Accessing tuple values
print("Name:", person[0])
print("Age:", person[1])

# If I try to change this, Python will throw an error
# person[1] = 30  # can't update a tuple



# Another tuple example
birth_info = ("Muhammad Rizwan", "15-10-1998", "Pakistan")
print("\nBirth info tuple:", birth_info)



# Quick summary for myself
print("\nList = changeable, slower, takes more memory")
print("Tuple = not changeable, faster, takes less memory")
