from brain_games.cli import welcome_user


def run_game(rules, generate_question):
    name = welcome_user()
    print(rules)
    for _ in range(3):
        question, correct_answer = generate_question()
        print(f"Question: {question}")
        answer = input("Your answer: ")
        if answer == str(correct_answer):
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")