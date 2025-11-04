from random import randint
import sys

dice= int(input("Hello, welcome to the dice roller! How many dice would you like to play with?"))
sides = int(input("How many sides per die?"))
if sides <= 1:
    print("Nice try, put a number greater than one.")
    sides = int(input("How many sides per die?"))
money = 100
print("You have $",money)
des = input("Do you want to bet?(y/n)")
if des == "y":
    what = input("What outcome do you want to bet on? Put 'even' to bet on the sum of the dice being an even number"
    " 'odd' to bet that the sum will be odd, or type the number that you think the sum will be. If you bet on even or" \
    " odd and win, you will gain money equal to your bet. If you bet on a number and win, you will gain money equal to" \
    " your bet times 4. Losing just loses you your bet.")
    amount = int(input("How much do you want to bet?"))


def roll(d, s):
    i =0
    rolls = []
    while i < d:
        z = randint(1,s)
        rolls.append(z)
        i += 1

    print("These are your results:")
    x=0
    for n in rolls:
        if n == s:
            print(n, "YAY, HIGH ROLL")
        else:
            print(n)
        x+= n
    print(f"Sum: {x}")
   
    return x

while True:
    x = roll(dice, sides)
    if what.lower() == "even":
        if x%2 ==0:
            money += amount
            print("Yay, you win!")
        else:
            money-= amount
            print("Shucks, you lost.")
    elif what.lower() == "odd":
        if x%2 !=0:
            money += amount
            print("Yay, you win!")
        else:
            money-= amount
            print("Shucks, you lost.")
    else:
        if x == int(what):
            money += amount*4
            print("Yay! YOU WIN!")
        else:
            money -= amount
            print("Well, you lost. Better luck next time.")
    print("You have $",money)
    again = input("Roll again?")
    if again.lower().strip() == ("y" or "yes"):
        dice = int(input(("How many dice?")))
        sides = int(input("How many sides per die?"))
        if sides <= 1:
            print("Nice try, put a number greater than one.")
            sides = int(input("How many sides per die?"))
        des = input("Do you want to bet?(y/n)")
        if des == "y":
            what = input("What outcome do you want to bet on? Put 'even' to bet on the sum of the dice being an even number"
            "'odd' to bet that the sum will be odd, or type the number that you think the sum will be. If you bet on even or" \
            "odd and win, you will gain money equal to your bet. If you bet on a number and win, you will gain money equal to" \
            "your bet times 4. Losing just loses you your bet.")
            amount = int(input("How much do you want to bet?"))
    else:
        if x < sides*dice/2:
            print("After that last roll, it makes sense.")
        elif x == sides*dice:
            print("Want to leave on a win, eh? Now scram")
            sys.exit()
        else:
            print("Understandable, have a good day.")
        break
