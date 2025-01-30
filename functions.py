def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3, 4))  # Output: 10


def add(num1, num2):
    print(num1 - num2)

add(7,3)    



# A function can take input values (parameters).
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")



# A function can return a value using the return statement.
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8



# Default Parameter Values(If a parameter has a default value, it becomes optional when calling the function)
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()        # Output: Hello, Guest!
greet("Alice") # Output: Hello, Alice!


# 
