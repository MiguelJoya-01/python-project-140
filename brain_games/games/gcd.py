from random import randint

RULES = "Find the greatest common divisor of given numbers."

MIN_NUMBER = 1
MAX_NUMBER = 100


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def generate_question():
    num1 = randint(MIN_NUMBER, MAX_NUMBER)
    num2 = randint(MIN_NUMBER, MAX_NUMBER)
    question = f"{num1} {num2}"
    correct_answer = gcd(num1, num2)
    return question, correct_answer
