"""Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
(Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out."""

# Exercise 9:
import random
import sys

ss = input("Type Start or Stop to Begin or Exit: ")
count = 0
if ss == "Stop" or ss == "stop":
    print("Bye! See you next time!")
    sys.exit()
elif ss == "Start" or ss == "start":
    while ss:
        num = random.randint(1, 9)
        print("A random number from 1 to 9 has been generated.")
        ans = 0
        while ans != num:
            ans = int(input("Type a number to guess: "))
            if ans > num:
                print("Your answer is too high.")
                retry = input("Do you want to try again? (Y/N) ")
                if retry == "Y" or retry == "y":
                    count += 1
                    continue
                elif retry == "N" or retry == "n":
                    print("It took you " + str(count) + " times but still could not get the answer!")
                    sys.exit()
                else:
                    print("Invalid input.")
            elif ans < num:
                print("Your answer is too low.")
                retry = input("Do you want to try again? (Y/N) ")
                if retry == "Y" or retry == "y":
                    count += 1
                    continue
                elif retry == "N" or retry == "n":
                    print("It took you " + str(count) + " times but still could not get the answer!")
                    sys.exit()
                else:
                    print("Invalid input.")
            elif ans == num:
                count += 1
                print("Congrats! You got it right. The number is " + str(num))
                print("It took you " + str(count) + " times to get the answer!")
                sys.exit()
else:
    print("Invalid input. Exiting...")
    sys.exit()