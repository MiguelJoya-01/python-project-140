from random import randint

from brain_games.engine import run_game

RULES = "Answer 'yes' if the number is even, otherwise answer 'no'."


def generate_question():
    num = randint(1, 100)
    correct_answer = "yes" if num % 2 == 0 else "no"
    return num, correct_answer


def play_even():
    run_game(RULES, generate_question)
