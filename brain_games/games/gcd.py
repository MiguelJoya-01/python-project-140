from random import randint

RULES = "Find the greatest common divisor of given numbers."


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def generate_question():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    question = f"{num1} {num2}"
    correct_answer = gcd(num1, num2)
    return question, correct_answer


