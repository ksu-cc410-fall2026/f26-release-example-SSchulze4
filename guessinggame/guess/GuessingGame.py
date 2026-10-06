"""Guessing game class.

Author: Russell Feldhausen russfeld@ksu.edu
Version: 0.1
"""

from typing import List
from guessinggame.guess.GuessResult import GuessResult


class GuessingGame:
    """Guessing game class."""

    def __init__(self, secret: str) -> None:
        """Constructor.

        Args:
            secret: the secret phrase to guess
        Raises:
            ValueError if the secret is not 5 characters
        """
        if len(secret) < 5:
            raise ValueError("Secret must be at least 5 characters long")
        self.__secret_phrase: str = secret
        self.__revealed_phrase: List[str] = ["_" if x.isalpha()
                                             else x for x in
                                             self.__secret_phrase]
        self.__guesses: List[str] = []
        self.__wrong_guesses: int = 0

    @property
    def revealed_phrase(self) -> str:
        """The revealed phrase."""
        return "".join(self.__revealed_phrase)

    @property
    def guesses(self) -> List[str]:
        """The list of guesses."""
        return self.__guesses.copy()

    @property
    def wrong_guesses(self) -> int:
        """The number of wrong guesses."""
        return self.__wrong_guesses

    @property
    def won(self) -> bool:
        """If the game is won."""
        return '_' not in self.__revealed_phrase

    @property
    def lost(self) -> bool:
        """If the game is lost."""
        return self.__wrong_guesses >= 7

    @property
    def in_progress(self) -> bool:
        """If the game is in progress."""
        return not (self.won or self.lost)

    def guess(self, c: str) -> GuessResult:
        """Guesses a character.

        Args:
            c: the character to guess
        Returns:
            a `GuessResult` value
        """
        if not c.isalpha():
            return GuessResult.NOTLEGAL
        c = c.lower()
        if c not in self.__guesses:
            self.__guesses.append(c)
            found: bool = False
            for i in range(0, len(self.__secret_phrase)):
                if self.__secret_phrase[i].lower() == c:
                    self.__revealed_phrase[i] = self.__secret_phrase[i]
                    found = True
            if not found:
                self.__wrong_guesses += 1
                return GuessResult.INCORRECT
            else:
                return GuessResult.CORRECT
        else:
            return GuessResult.MULTIPLE
