# Creating a list
my_list = [10, "hello", 3.14, True]

# Accessing elements(List Indexing)
print(my_list[1])  # Output: hello

# Modifying elements
my_list[0] = 99
print(my_list)  # Output: [99, 'hello', 3.14, True]

#Print Lists Length
print(len(my_list)) # Output: 4

#Slicing a Lists
print(my_list[1:4]) #Creates a new list with elements at index 1,2,3

# Adding elements
my_list.append("Python")
print(my_list)  # Output: [99, 'hello', 3.14, True, 'Python']

# Removing elements
my_list.remove(3.14)
print(my_list)  # Output: [99, 'hello', True, 'Python']

# Iterating through a list and printing all elements in a List.
for item in my_list:
    print(item)

#Checking if an element is present in a List
is_present = "boy" in my_list
print(is_present)
