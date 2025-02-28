# for i in range(1, 10):
#     print("current value is:", i)

# name = eval(input("enter your name:"))
# print("your name is:", name)

# for i in range(4):
#     num = eval(input("Enter a number:"))
#     print("The square of the number is:", num*num)
# print("The Loop is finished")
# Result: The Loop is finished

# for i in range(5, 0, -1):
#     print(i, end=" ")
# print("Blast off!!!")    
# Result: 5 4 3 2 1 Blast off!!!

# for i in range(101):
#     print("Olusegun!!!", end=" ")
# Resutl: ["Olusegun!!!"] * 101


# Write a program that uses exactly four for loops to print the sequence of letters below.
#  AAAAAAAAAABBBBBBBCDCDCDCDEFFFFFFG
# for i in range(11):
#     print("A", end=" ")
# for i in range(8):
#     print("B", end=" ")
# for i in range(4):
#     print("C", end=" ")  
#     print("D", end=" ")  
# print("E", end=" ")     
# for i in range(6):
#     print("F", end=" ")
# print("G", end=" ")     
#Result: AAAAAAAAAABBBBBBBCDCDCDCDEFFFFFFG

import random
# x = randint(1,20)
# print(x)
# Result: print a random number between 1 and 20

# from math import sin, pi, cos
# print("sin60/2 + cos60/2:", sin(60/2) + cos(60/2))

#Write a program that generates and prints 50 random integers, each between 3 and 6.
# for i in range(51):
#    print(randint(3, 6), end="")
# Result: 544346553544554355644656543655666334633665435645435


# Write a program that generates a random number, x, between 1 and 50, a random number y
#  between 2 and 5, and computes xy
# x = random.randint(1,50)
# y = random.randint(2,5)
# print("x is " f"{x}", "y is " f"{y}")
# print(x**y)

# Write a program that generates a random number between 1 and 10 and prints your name
# that many times
# x = random.randint(1, 10)
# for i in range(x):
#     print("Hello")
# Result: print Hello x times

# A program to check for an ATM card number
# num = random.randint(1000, 9999)
# GuessATM = eval(input("Enter your ATM card number: "))
# if GuessATM == num:
#     print("Correct, you guessed right, let's proceed")
# else:
#     print("Wrong, you guessed wrong, try again")
# Result: if the user guess the correct number, it will print "Correct, you guessed right, let's proceed"


ATM_Pin = 1234
User_Guess = eval(input("Enter your pin here: " ))
while ATM_Pin != User_Guess:
    print("Wrong Pin, try again")
    User_Guess = eval(input("Enter your pin here: " )) 
if  ATM_Pin == User_Guess:
    print("Pin Correct, let's proceed")   