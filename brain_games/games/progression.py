from random import randint

RULES = "What number is missing in the progression?"


def generate_question():
    progression_length = randint(5, 10)
    start = randint(1, 20)
    step = randint(1, 10)

    question = []

    for i in range(progression_length):
        question.append(start + step * i)

    correct_answer_index = randint(0, progression_length - 1)
    correct_answer = question[correct_answer_index]
    question[correct_answer_index] = ".."

    question = " ".join(map(str, question))

    return question, str(correct_answer)


