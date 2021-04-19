import random

print("Welcome to guessing number Game")

num = random.randrange(0,10) #to generate random number between 0-10

while(True):
    guess = int(input("guess the number between 0-10 : "))
    
    if guess == num:
        print("You Won")
        break
    elif guess > num:
        print("\nValueTooLargeError")
        print("Try Again \n")
    else:
        print("ValueTooSmallError")
        print("Try Again \n")
print("BYE - BYE")
