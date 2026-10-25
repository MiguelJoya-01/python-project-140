from brain_games.engine import run_game
from brain_games.games.even import RULES, generate_question


def brain_even():
    run_game(RULES, generate_question)


def main():
    brain_even()


if __name__ == "__main__":
    main()
