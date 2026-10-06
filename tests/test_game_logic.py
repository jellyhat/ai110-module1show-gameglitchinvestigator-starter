from pathlib import Path

from streamlit.testing.v1 import AppTest

from logic_utils import (
    check_guess,
    generate_secret,
    get_attempt_limit,
    parse_guess,
)

def test_winning_guess():
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")

def test_guess_too_high():
    result = check_guess(60, 50)
    assert result == ("Too High", "📉 Go LOWER!")

def test_guess_too_low():
    result = check_guess(40, 50)
    assert result == ("Too Low", "📈 Go HIGHER!")

def test_feedback_compares_guesses_numerically():
    assert check_guess(9, 10) == ("Too Low", "📈 Go HIGHER!")
    assert check_guess(10, 9) == ("Too High", "📉 Go LOWER!")


def test_higher_lower_feedback_fix():
    too_high, high_message = check_guess(60, 50)
    too_low, low_message = check_guess(40, 50)

    assert too_high == "Too High"
    assert "LOWER" in high_message
    assert too_low == "Too Low"
    assert "HIGHER" in low_message


def test_invalid_guess_is_rejected():
    assert parse_guess("not a number") == (False, None, "That is not a whole number.")
    assert parse_guess(" ") == (False, None, "Enter a guess.")


def test_difficulty_change_starts_new_game():
    app = AppTest.from_file(str(Path(__file__).parents[1] / "app.py")).run()
    app.session_state["attempts"] = 3
    app.session_state["score"] = 25
    app.session_state["history"] = [12, 45, 67]

    app.selectbox[0].set_value("Easy").run()

    assert app.session_state["difficulty"] == "Easy"
    assert app.session_state["attempts"] == 0
    assert app.session_state["score"] == 0
    assert app.session_state["history"] == []
    assert 1 <= app.session_state["secret"] <= 20
    assert any(
        "Difficulty changed. A new game is starting" in message.value
        for message in app.info
    )


def test_invalid_input_does_not_use_attempt():
    app = AppTest.from_file(str(Path(__file__).parents[1] / "app.py")).run()
    app.session_state["attempts"] = 2
    app.session_state["history"] = [12, 45]

    app.text_input(key="guess_input_Normal").set_value("not a number")
    app.button[0].click().run()

    assert app.session_state["attempts"] == 2
    assert app.session_state["history"] == [12, 45]
    assert any("That is not a whole number." in error.value for error in app.error)


def test_attempts_left_updates_after_valid_guess():
    app = AppTest.from_file(str(Path(__file__).parents[1] / "app.py"))
    app.session_state["secret"] = 50
    app.run()

    app.text_input(key="guess_input_Normal").set_value("40")
    app.button[0].click().run()

    assert app.session_state["attempts"] == 1
    assert any("Attempts left: 7" in message.value for message in app.info)


def test_attempt_limits_by_difficulty():
    assert get_attempt_limit("Easy") == 6
    assert get_attempt_limit("Normal") == 8
    assert get_attempt_limit("Hard") == 5

def test_generated_secret_stays_inclusive_range():
    assert generate_secret(7, 7) == 7
