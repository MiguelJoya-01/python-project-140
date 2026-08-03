from brain_games.engine import run_game
from brain_games.games.progression import RULES, generate_question


def brain_progression():
    run_game(RULES, generate_question)
    
    
def main():
    brain_progression()