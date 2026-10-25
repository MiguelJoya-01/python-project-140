from random import randint

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'

MIN_NUMBER = 1
MAX_NUMBER = 100


def generate_question():
    num = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = "yes" if num % 2 == 0 else "no"
    return num, correct_answer
