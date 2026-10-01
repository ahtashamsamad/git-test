"""Tests for the guessing game."""

from guessing_game import check_guess, is_valid_guess


def test_guess_too_low():
    """Test when the guess is lower than the secret number."""
    assert check_guess(50, 30) == "Too low"


def test_guess_too_high():
    """Test when the guess is higher than the secret number."""
    assert check_guess(50, 70) == "Too high"


def test_guess_correct():
    """Test when the guess matches the secret number."""
    assert check_guess(50, 50) == "Correct"


def test_valid_guess():
    """Test valid guesses."""
    assert is_valid_guess(1) is True
    assert is_valid_guess(50) is True
    assert is_valid_guess(100) is True


def test_invalid_guess():
    """Test invalid guesses."""
    assert is_valid_guess(0) is False
    assert is_valid_guess(101) is False
