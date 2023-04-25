"""
In Bagels, a deductive logic game, you must guess a secret three-digit number based on clues.
The game offers one of the following hints in response to your guess:
    “Pico” when your guess has a correct digit in the wrong place,
    “Fermi” when your guess has a correct digit in the correct place, and
    “Bagels” if your guess has no correct digits.
You have 10 tries to guess the secret number.
"""
###IMPORTS
import random

###GLOBAL VARS###
#allowed amount of guessing
MAX_GUESSES = 10
#lenth of digit for guessing
NUM_DIGITS = 3

###MAIN FUNC###
def main():
    print('''Bagels, a deductive logic game. I am thinking of a {}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say:    That means:
        Pico        One digit is correct but in the wrong position.
        Fermi       One digit is correct and in the right position.
        Bagels      No digit is correct.

    For example, if the secret number was 248 and your guess was 843, the
    clues would be Fermi Pico.'''.format(NUM_DIGITS))

    while True:
        #guess a digit
        secretNum = getSecretNum()
        print("Let's start! I got a number for you")
        print(f"You have {MAX_GUESSES} guess(es) left")

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = input(f"Enter your {numGuesses} guess: ")
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print("Your input is not valid, enter again")
                guess = input(f"Enter your {numGuesses} guess: ")

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                print(clues)
                break
            if numGuesses > MAX_GUESSES:
                print("You ran out of guesses")
                print(f"The asnwer was {secretNum}")

        print("Would like to play again? (Y/N)")
        if not input().lower().startswith("y"):
            break
    print("Thank for playing!")



###getSecretNum - generating a number for user's guessing###
def getSecretNum():
    numbers = [0,1,2,3,4,5,6,7,8,9]
    random.shuffle(numbers)
    secretNum = ""

    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


###getClues - cluing to user based on his input###
def getClues(guess, secretNum):
    if guess == secretNum:
        return "Congratulations! You got it!"

    clues = []
    for i in range(len(guess)):
        #if correct digit in correct place
        if guess[i] == secretNum[i]:
            clues.append("Fermi")
        #if for correct digit in wrong place
        elif guess[i] in secretNum:
            clues.append("Pico")
    #if wrong digit in wrong place
    if len(clues) == 0:
        return "Bogels"
    else:
        clues.sort()
        return " ".join(clues)










###of the prog is run (not imported), run the game###
if __name__ == "__main__":
    main()