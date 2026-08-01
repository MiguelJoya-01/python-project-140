from brain_games.engine import run_game
from brain_games.games.gcd import RULES, generate_question


def brain_gcd():
    run_game(RULES, generate_question)
    
    
def main():
    brain_gcd()