import random
from typing import Optional, Tuple


ATTEMPT_LIMITS = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}


def get_range_for_difficulty(difficulty: str) -> Tuple[int, int]:
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def get_attempt_limit(difficulty: str) -> int:
    """Return the number of allowed guesses for a difficulty."""
    return ATTEMPT_LIMITS[difficulty]


def generate_secret(low: int, high: int) -> int:
    """Choose a secret number from the inclusive range."""
    return random.randint(low, high)


def parse_guess(raw: Optional[str]) -> Tuple[bool, Optional[int], Optional[str]]:
    """Parse user input into an integer guess and return any validation error."""
    if raw is None or not raw.strip():
        return False, None, "Enter a guess."

    try:
        return True, int(raw.strip()), None
    except ValueError:
        return False, None, "That is not a whole number."


def check_guess(guess: int, secret: int) -> Tuple[str, str]:
    """Compare a guess with the secret and return its outcome and feedback."""
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int) -> int:
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
