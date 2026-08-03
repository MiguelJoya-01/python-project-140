from brain_games.engine import run_game
from brain_games.games.prime import RULES, generate_question


def brain_prime():
    run_game(RULES, generate_question)
    
    
def main():
    brain_prime()
