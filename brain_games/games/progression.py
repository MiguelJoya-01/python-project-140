from random import randint

RULES = "What number is missing in the progression?"

MIN_PROGRESSION_LENGTH = 5
MAX_PROGRESSION_LENGTH = 10

MIN_START = 1
MAX_START = 20

MIN_STEP = 1
MAX_STEP = 10


def generate_question():
    progression_length = randint(
        MIN_PROGRESSION_LENGTH, MAX_PROGRESSION_LENGTH
    )
    start = randint(MIN_START, MAX_START)
    step = randint(MIN_STEP, MAX_STEP)

    question = []

    for i in range(progression_length):
        question.append(start + step * i)

    correct_answer_index = randint(0, progression_length - 1)
    correct_answer = question[correct_answer_index]
    question[correct_answer_index] = ".."

    question = " ".join(map(str, question))

    return question, str(correct_answer)

