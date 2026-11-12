import random
def level():
    diff=str(input("Difficulty: [EX:Expert][ME:Medium][ES:Easy]"))
    return diff
def difficulty():
    diff=level()
    if diff == "ex":
        i=int(4)
    elif diff == "es":
        i=int(9)
    else:
        i=int(6)
    return i
def ask_val():
    while True:
        try:
            value_p = int(input("Enter a number between 0 and 100: "))
            if 0 <= value_p and value_p <= 100:
                return value_p
            else:
                print(" Number must be between 0 and 100.")
        except ValueError:
            print(" please enter a valid number")
def game():
    i=difficulty()
    value_p = ask_val()
    x = random.randint(0, 100)
    
    while value_p != x and i >= 1:
        if value_p < x:
            print("Too low")
        else:
            print("Too high")
        print("Attempts left:", i)
        i -= 1
        value_p = ask_val()
    if value_p == x:
        print("Congratulations! You guessed the number.")
    else:
        print("You lost!")
        print("The number was:", x)
    play=str(input('do you wanna play again: [Y:yes][N:no]'))
    if play == 'Y' or play == 'yes' or play == 'y' or play == 'Yes' or play == 'YES':
        game()
    else:
        print("thanks see you soon")
    
game()

    