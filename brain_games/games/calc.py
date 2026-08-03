from random import randint

RULES = "What is the result of the expression?"


def generate_question():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    operator = randint(1, 3)
    if operator == 1:
        result = number1 + number2
        question = f"{number1} + {number2}"
    elif operator == 2:
        result = number1 - number2
        question = f"{number1} - {number2}"
    else:
        result = number1 * number2
        question = f"{number1} * {number2}"
    return question, str(result)

