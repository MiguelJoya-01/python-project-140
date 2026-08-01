from brain_games.engine import run_game
from brain_games.games.calc import RULES, generate_question


def brain_calc():
    run_game(RULES, generate_question)

       
def main():
    brain_calc()