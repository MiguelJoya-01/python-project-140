from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'

MIN_NUMBER = 1
MAX_NUMBER = 100


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def generate_question():
    number = randint(MIN_NUMBER, MAX_NUMBER)
    question = str(number)
    answer = "yes" if is_prime(number) else "no"
    return question, answer
