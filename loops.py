
# Loops in Python (for and while)

## Introduction

"""Loops are a fundamental concept in programming, and they allow you 
to perform repetitive tasks efficiently. In Python, there are two primary types 
of loops: "for" and "while."""

## For Loop

"""The "for" loop is used to iterate over a sequence (such as a list, tuple, string, or range) 
and execute a set of statements for each item in the sequence. The loop continues until all
items in the sequence have been processed."""

#for variable in sequence:
    # Code to be executed for each item in the sequence

fruits = ["banana", "mango", "pawpaw", "Pawpaw", "Orange"]
for fruit in fruits:
    print(fruit)


#Using range() Function
for i in fruits:
    print(i)
    print("Sam")

# Looping Through a String
for letter in "PYTHON":
    print(letter)



## ================== While Loop==========
#A while loop runs as long as a condition remains True.

x = 0 
while x <= 7:
    print(x)
    x += 1



##============= Loop Control Statements ============
#======== break statement =============== 
#The "break" statement is used to exit a loop prematurely. When the "break" statement is encountered, the loop is terminated, 
# and the program continues with the next statement after the loop.

for i in range(10):
    if i == 5:
        break
    print(i)

"""x = 2
while x <= 10:
    print(x)
    if x == 5:
        continue
    x += 1"""

x = 1
while x <= 10:
    if x == 5:
        break
    print(x)
    x += 1


print("continue statement")
x = 2
while x <= 10:
    if x == 5:
        x += 1
        continue
    print(x)
    x += 1

#Print Numbers from 10 to 1 in Reverse
for num in range(10, 0, -1):
    print(num)


password = ""
while password != "1234":  # Runs indefinitely until the correct password is entered
    password = input("Enter password: ")

print("Access granted!")

#Tasks

#
#Print Odd Numbers from 1 to 10
#Print Even Numbers from 1 to 10
#Print Numbers from 1 to 10, but Stop at 7
#Print Numbers from 1 to 10, Skipping 5
#Print Numbers from 1 to 10 Using while Loop
#Print Multiples of 3 from 1 to 20
#Print Numbers Until the Sum Reaches 20
#    #
