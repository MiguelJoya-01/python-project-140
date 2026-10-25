from random import randint

RULES = "What is the result of the expression?"

MIN_NUMBER = 1
MAX_NUMBER = 100
MIN_OPERATION = 1
MAX_OPERATION = 3


def generate_question():
    number1 = randint(MIN_NUMBER, MAX_NUMBER)
    number2 = randint(MIN_NUMBER, MAX_NUMBER)
    operator = randint(MIN_OPERATION, MAX_OPERATION)

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
