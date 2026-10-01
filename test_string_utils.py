"""Tests for string utility functions."""

from string_utils import is_palindrome


def test_palindrome_word():
    """Test a normal palindrome word."""
    assert is_palindrome("madam") is True


def test_palindrome_racecar():
    """Test another palindrome."""
    assert is_palindrome("racecar") is True


def test_not_palindrome():
    """Test a word that is not a palindrome."""
    assert is_palindrome("hello") is False


def test_case_insensitive():
    """Test that uppercase letters are handled."""
    assert is_palindrome("Madam") is True


def test_palindrome_with_spaces():
    """Test palindrome containing spaces."""
    assert is_palindrome("Never Odd") is True


def test_empty_string():
    """Test an empty string."""
    assert is_palindrome("") is True