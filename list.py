students = ["Kai-samba", "Foday", "Sharon"]
print(students)

# Accessing items in a list by their index
print(f"My bestfriend is {students[0]}")
print(f"My bestfriend is {students[1]}")
print(f"My bestfriend is {students[2]}")

# Get the index of an item in a list
print(students.index("Kai-samba"))
print(f"The total items in the list is: {len(students)}")

# Add items to a list
students.append("Isatu")
print(students)
students += ["Kadiatu", "John", "Bintu"]

# Add items to a list
print(students)
students.insert(4, "Donald")

# Extending a list
fruits = ["Apple", "Banana", "Mango"]
students.extend(fruits)

# Removing an item from a list
fruits.remove("Mango")

students.pop()
students.pop()
students.pop()
print(students)
