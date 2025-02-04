
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

for i in range(10):
    if i == 5:
        break
    print(i)