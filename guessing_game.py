"""Number guessing game logic."""


def check_guess(secret_number, player_guess):
    """Compare the player's guess with the secret number."""
    if player_guess < secret_number:
        return "Too low"

    if player_guess > secret_number:
        return "Too high"

    return "Correct"


def is_valid_guess(guess):
    """Return True if the guess is between 1 and 100."""
    return 1 <= guess <= 100
