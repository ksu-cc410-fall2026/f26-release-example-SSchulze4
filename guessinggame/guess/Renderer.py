"""Guessing game renderer.

Author: Russell Feldhausen russfeld@ksu.edu
Version: 0.1
"""

from typing import List
from guessinggame.guess.GuessResult import GuessResult


class Renderer:
    """Guessing game renderer."""

    @staticmethod
    def print_hello() -> None:
        """Print hello message."""
        print("Welcome to Lobster!")

    @staticmethod
    def print_lobster(guesses: int) -> None:
        """Print lobster.

        Args:
            guesses: the number of wrong guesses
        """
        lobster: List[str] = ["|~~~~~~~~|",
                              "| (]  [) |",
                              "|  \\oo/  |",
                              "| >{^^}< |",
                              "| >{^^}< |",
                              "|  {^^}  |",
                              "|  {^^}  |",
                              "|  /MM\\  |",
                              "|________|"]
        empty: List[str] = ["|~~~~~~~~|",
                            "|        |",
                            "|        |",
                            "|        |",
                            "|        |",
                            "|        |",
                            "|        |",
                            "|        |",
                            "|________|"]
        for i in range(0, guesses + 1):
            print(lobster[i])
        for i in range(guesses + 1, len(empty)):
            print(empty[i])

    @staticmethod
    def print_message(good: GuessResult) -> None:
        """Print a result message."""
        if good == GuessResult.CORRECT:
            print("Great Guess!")
        elif good == GuessResult.INCORRECT:
            print("Oh no! Things are heating up!")
        elif good == GuessResult.MULTIPLE:
            print("You've already guessed that letter!")
        elif good == GuessResult.NOTLEGAL:
            print("That's not a letter!")

    @staticmethod
    def print_phrase(phrase: str) -> None:
        """Print a secret phrase."""
        print("Your phrase to guess:")
        print(phrase)

    @staticmethod
    def print_guesses(guesses: List[str]) -> None:
        """Print the list of guesses."""
        print("Your previous guesses are:")
        print(guesses)

    @staticmethod
    def get_guess() -> str:
        """Get a guess from the user."""
        c: str = input("Enter a letter to guess: ")
        return c

    @staticmethod
    def clear_screen() -> None:
        """Clear the screen."""
        print("\033\143")

    @staticmethod
    def print_win() -> None:
        """Print winning message."""
        print("You Won!")

    @staticmethod
    def print_loss() -> None:
        """Print losing message."""
        print("You Lost!")
