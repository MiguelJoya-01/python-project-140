from random import randint

from brain_games.cli import welcome_user


def brain_even():
    name = welcome_user()
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    for _ in range(3):
        number = randint(1, 100)
        print(f"Question: {number}")
        answer = input("Your answer: ")
        if number % 2 == 0 and answer == "yes":
            print("Correct!")
        elif number % 2 != 0 and answer == "no":
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{'yes' if number % 2 == 0 else 'no'}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
    
    
def main():
    brain_even()