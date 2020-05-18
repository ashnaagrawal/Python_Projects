import random

min = 1
max = 6


def dice():
    data_valid = False
    while data_valid == False :
        roll_again = str(input("If you want to play roll the dice, Please type 'yes' or 'y':"))
        roll_again = roll_again.lower()    
        if roll_again == "yes" or roll_again == "y" :
            data_valid = True
        
        else:
            print("Typed value is not correct. Please re-type  ")
            continue
        
roll_again = str(input("If you want to roll the dice, Please type 'yes' or 'y':"))
roll_again = roll_again.lower()

while roll_again == "yes" or roll_again == "y":
    num = random.randint(min,max)
    print("Your number is:" , num)
    if num == 6 :
        num1 = random.randint(min,max)
        print("Your number is :",num1)
        if num1 == 6:
            num2  = random.randint(min,max)
            print("Your number is:",num2)
            if num1 == num2:
                print("Your all the chances are cancelled.")
                print("Roll your dice again.")
                roll_again = input("If you want to roll the dice, Please type 'yes' or 'y':")
    dice()
           

