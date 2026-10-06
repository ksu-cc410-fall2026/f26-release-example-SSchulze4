"""Test class for guessing game.

Author: Russell Feldhausen russfeld@ksu.edu
Version: 0.1
"""
from guessinggame.guess.GuessingGame import GuessingGame
from guessinggame.guess.GuessResult import GuessResult
import pytest


class TestGuessingGame:
    """Test guessing game."""

    def test_guesses_should_be_empty_at_start_of_game(self):
        """Test method."""
        game = GuessingGame("secret")
        assert len(game.guesses) == 0
        # assert_that(game.guesses, is_(empty()))

    @pytest.mark.parametrize("secret", ["", "a", "aa", "aaa", "aaaa"])
    def test_secret_phrase_must_be_at_least_5_characters_long(self, secret):
        """Test method."""
        with pytest.raises(ValueError):
            game = GuessingGame(secret)
            assert game is None

    def test_wrong_guesses_should_start_at_zero(self):
        """Test method."""
        game = GuessingGame("secret")
        assert game.wrong_guesses == 0

    def test_new_game_should_not_be_won(self):
        """Test method."""
        game = GuessingGame("secret")
        assert not game.won

    def test_new_game_should_not_be_lost(self):
        """Test method."""
        game = GuessingGame("secret")
        assert not game.lost

    def test_new_game_should_be_in_progreses(self):
        """Test method."""
        game = GuessingGame("secret")
        assert game.in_progress

    @pytest.mark.parametrize("secret,revealed", [
        ("Hello World", "_____ _____"),
        ("Don't Forget Your Towel", "___'_ ______ ____ _____"),
        ("John Jacob Jingleheimer Schmidt",
         "____ _____ ____________ _______")])
    def test_secret_phrase_should_encode_provided_secret(self, secret,
                                                         revealed):
        """Test method."""
        game = GuessingGame(secret)
        assert revealed == game.revealed_phrase

    @pytest.mark.parametrize("guess", ['k', 's', 'u'])
    def test_guesses_should_be_added_to_previous_guesses(self, guess):
        """Test method."""
        game = GuessingGame("secret")
        game.guess(guess)
        assert guess in game.guesses

    def test_wrong_guesses_should_increment_wrong_guesses(self):
        """Test method."""
        game = GuessingGame("secret")
        game.guess('a')
        assert game.wrong_guesses == 1
        game.guess('b')
        assert game.wrong_guesses == 2
        game.guess('d')
        assert game.wrong_guesses == 3
        game.guess('f')
        assert game.wrong_guesses == 4
        game.guess('g')
        assert game.wrong_guesses == 5
        game.guess('h')
        assert game.wrong_guesses == 6

    def test_seven_wrong_guesses_should_end_game(self):
        """Test method."""
        game = GuessingGame("secret")
        game.guess('a')
        game.guess('b')
        game.guess('d')
        game.guess('f')
        game.guess('g')
        game.guess('h')
        game.guess('i')
        assert not game.in_progress

    def test_seven_wrong_guesses_should_lose(self):
        """Test method."""
        game = GuessingGame("secret")
        game.guess('a')
        game.guess('b')
        game.guess('d')
        game.guess('f')
        game.guess('g')
        game.guess('h')
        game.guess('i')
        assert game.lost

    def test_correct_guesses_should_end_game(self):
        """Test method."""
        game = GuessingGame("secret")
        game.guess('s')
        game.guess('e')
        game.guess('c')
        game.guess('r')
        # game.guess('e')
        game.guess('t')
        assert not game.in_progress

    def test_correct_guesses_should_win(self):
        """Test method."""
        game = GuessingGame("secret")
        game.guess('s')
        game.guess('e')
        game.guess('c')
        game.guess('r')
        # game.guess('e')
        game.guess('t')
        assert game.won

    def test_guessing_same_character_should_not_count(self):
        """Test method."""
        game = GuessingGame("secret")
        game.guess('s')
        assert len(game.guesses) == 1
        game.guess('s')
        assert len(game.guesses) == 1
        game.guess('a')
        assert game.wrong_guesses == 1
        game.guess('a')
        assert game.wrong_guesses == 1

    @pytest.mark.parametrize("guess", ['!', '3', ' '])
    def test_guess_should_be_a_letter(self, guess):
        """Test method."""
        game = GuessingGame("secret")
        assert game.guess(guess) == GuessResult.NOTLEGAL

    @pytest.mark.parametrize("guess", ['s', 'e', 'c', 'r', 't'])
    def test_correct_guess_should_return_correct(self, guess):
        """Test method."""
        game = GuessingGame("secret")
        assert game.guess(guess) == GuessResult.CORRECT

    @pytest.mark.parametrize("guess", ['a', 'b', 'd', 'f', 'g'])
    def test_incorrect_guess_should_return_incorrect(self, guess):
        """Test method."""
        game = GuessingGame("secret")
        assert game.guess(guess) == GuessResult.INCORRECT

    @pytest.mark.parametrize("guess", ['a', 'b', 'c', 'd', 'e'])
    def test_multiple_guess_should_return_multiple(self, guess):
        """Test method."""
        game = GuessingGame("secret")
        game.guess(guess)
        assert game.guess(guess) == GuessResult.MULTIPLE

    def test_guesses_should_be_case_insensitive(self):
        """Test method."""
        game = GuessingGame("secret")
        assert game.guess('s') == GuessResult.CORRECT
        assert game.guess('E') == GuessResult.CORRECT
