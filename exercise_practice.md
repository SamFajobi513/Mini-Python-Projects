num = random.randint(1000, 9999)
GuessATM = eval(input("Enter your ATM card number:"))
if GuessATM == num:
    print("Correct, you guessed right, let's proceed")


ATM_Pin = 1234
User_Guess = eval(input("enter your pin here: " ))
while ATM_Pin != User_Guess:
    print("Wrong Pin, try again")
    User_Guess = eval(input("enter your pin here: " )) 
if  ATM_Pin == User_Guess:
    print("Pin Correct, let proceed")   