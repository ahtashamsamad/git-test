"""String utility functions."""


def is_palindrome(text):
    """Return True if text reads the same forwards and backwards."""
    text = text.lower().replace(" ", "")
    return text == text[::-1]
