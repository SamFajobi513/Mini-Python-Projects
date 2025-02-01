# Creating a list
my_list = [10, "hello", 3.14, True]

# Accessing elements
print(my_list[1])  # Output: hello

# Modifying elements
my_list[0] = 99
print(my_list)  # Output: [99, 'hello', 3.14, True]

# Adding elements
my_list.append("Python")
print(my_list)  # Output: [99, 'hello', 3.14, True, 'Python']

# Removing elements
my_list.remove(3.14)
print(my_list)  # Output: [99, 'hello', True, 'Python']

# Iterating through a list
for item in my_list:
    print(item)
