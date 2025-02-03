#===============================Lists=======================================
## What is a List?
#A list is a fundamental data structure in programming that allows you to store a 
# collection of items. Lists are ordered and can contain elements of various data types, 
# such as numbers, strings, and objects.

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



#=========================================Tuples=================================
#Lists and Tuples are similar, however, lists are mutable while 
#Definition: A tuple is an immutable, ordered collection of items. 
#Tuples can also contain elements of different data types.
#Syntax: Tuples are defined using parentheses ().

# Creating a tuple
my_tuple = (10, "hello", 3.14, True)

# Accessing Elements
print(my_tuple[1])  # Output: hello

# Tuple Length
print(len(my_tuple))  # Output: 4

# Slicing a Tuple
print(my_tuple[1:4])  # Output: ('hello', 3.14, True)

# Iterating through the tuple
for item in my_tuple:
    print(item)