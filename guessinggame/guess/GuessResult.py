"""Guess Result Enum.

Author: Russell Feldhausen russfeld@ksu.edu
Version: 0.1
"""

from enum import Enum


class GuessResult(Enum):
    """Guess result enum."""
    CORRECT = 1
    INCORRECT = 2
    MULTIPLE = 3
    NOTLEGAL = 4
