# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
Enter does not work|Enter would be the same as submit for each guess |Nothing happened |none | |
|The hints were the opposote |The hints should be accurate based on the guess and the answer |The hints were in reverse | none|
|Non valid inputs used an attempt |It should just say that its a wrong attempt and not increment your attempts |It did infact take your attempts |seen in console log as put in the array of attempts |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I used the Copilot in VS code (gpt-6-luna).
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

It found that there was a lot of incorrect logic randomly (such as even numbered guesses being treated differently) and corrected that logic. I tested it by running the app again and making sure. It also suggested to put the submit form in a Streamlit form, I accepted that change and it worked well when I was testing input.
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

I had asked the AI to not use up attempts on non-number inputs and it displayed the attempts left on top. However I noticed upon testing that after this, the attempts left did not update instantly after each guess and needed it to fix itself.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I read the logic of the code it changed and also tested the program myself locally.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.


To check the logic on hints was correct, I manually tested based on the number in the dev log to see if it was giving correct hints. It was.
- Did AI help you design or understand any tests? How?


I saw the new tests that it created after the fixes and could see the logic in what it was testing.


---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Much better for updating the UI per guess (or input state change here).

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

Testing the finished product yourself, asking AI why logic is wrong is good so it links to directly what function is probably wrong. This is good also if you use AI to fix something so you can add a comment for future reviewers to know which lines were entrusted to AI.
- What is one thing you would do differently next time you work with AI on a coding task?


Asking it to write itself own tests so you can iterate upon them.
- In one or two sentences, describe how this project changed the way you think about AI generated code.


It's not perfect since it quite literally listens to you. If you ask to change one bug it will not look over your whole document to fix a related bug, you have to be thorough.
