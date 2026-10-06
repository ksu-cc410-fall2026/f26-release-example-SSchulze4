"""Main class for guessing game.

Author: Russell Feldhausen russfeld@ksu.edu
Version: 0.1
"""

import random
from guessinggame.guess.GuessingGame import GuessingGame
from guessinggame.guess.Renderer import Renderer
from typing import List


class Main:
    """Main class for guessing game."""

    @staticmethod
    def main(args: List[str]) -> None:
        """Main method.

        Args:
            args: the command-line arguments
        """
        with open("phrases.txt") as file:
            phrases: List[str] = [line.strip() for line in file]
        index: int = random.randrange(len(phrases))
        game: GuessingGame = GuessingGame(phrases[index])
        Renderer.clear_screen()
        Renderer.print_hello()

        while game.in_progress:
            Renderer.print_lobster(game.wrong_guesses)
            Renderer.print_phrase(game.revealed_phrase)
            Renderer.print_guesses(game.guesses)
            c: str = Renderer.get_guess()
            Renderer.clear_screen()
            Renderer.print_message(game.guess(c))

        if game.won:
            Renderer.print_win()
        if game.lost:
            Renderer.print_loss()
