# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.

The game's purpose is to take a user's guess and help them get closer to the 'secret' number generated randomly. The user should be getting hints whether they need to guess a higher or lower number before they run out of attempts (Based on difficulty) and lose the game. The game also logs their points based on their guesses.
- [x] Detail which bugs you found.

I found the hints were given in an incorrect way, it told the user the opposite things, and it used attempts for non valid attempts (not explicitly a bug but i wanted to fix this). It would also not update on enter immediately despite showing that you could use the enter key. 
- [x] Explain what fixes you applied.

Fixed the logic and ui display on the hints that were incorrect. In addition, did not let the user change the difficulty in the middle of the game without changing gamestate, now it restarts a new game. It also moved the input into a streamlit form. 

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User may change difficulty setting on left but game starts on Normal difficulty with 8 attempts to guess a number from 1 - 100.
2. User can enter a guess in the text input box, they put 88.
3. User can press enter or press a submit guess button below the input. The UI shows that the guess is too low (displays Go LOWER!). Attempt was logged and it shows attempts left : 7
4. User enters a new number, 44 and submits guess. The UI displays Go HIGHER and attempt increments.
5. User enters 43 and submits guess. Balloons fly on screen, UI displays it was Correct and another display shows that the user won and their final score (50).

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
