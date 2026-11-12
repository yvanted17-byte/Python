# Number Guessing Game

A simple, beginner-friendly console game written in Python.  
The computer picks a random number, and the player has a limited number of attempts to guess it — with **"Too Low"** / **"Too High"** hints after every wrong guess.


---

## Table of Contents

- [About the Project](#-about-the-project)
- [Learning Objectives](#-learning-objectives)
- [Concepts Covered](#-concepts-covered)
- [Game Rules](#-game-rules)
- [Project Structure](#-project-structure)
- [Installation & Usage](#-installation--usage)
- [Functional Requirements](#-functional-requirements)


---

## About the Project

**Number Guessing Game** is a small interactive console program.  
The computer draws a random number inside a fixed range. The player must find it within a limited number of valid attempts.  
After every wrong guess, the program indicates whether the guess was **Too Low** or **Too High**, guiding the player toward the correct answer.

The project is intentionally simple — its purpose is to practise **control flow** (loops and conditions) and **robust input handling** rather than to build a complex application.

---

## Learning Objectives

By the end of this project, the developer should be able to:

- Build an interactive game loop that runs until a win/lose condition is met.
- Use `random.randint()` to generate unpredictable data.
- Validate user input with `try / except` and range checks.
- Combine `while`, `if / elif / else` and a counter to enforce a limited number of attempts.
- Keep a program running across multiple games (replay) without duplicating code.
- Write code that never crashes on bad input.

---

## Concepts Covered

| Concept | Where it is used |
|---|---|
| `random.randint(a, b)` | Generating the secret number |
| `while` loop | Input validation loop and game loop |
| `for` loop *(improved version)* | Attempt counter |
| `if / elif / else` | Comparison of guess against the secret |
| `int(input())` | Reading and converting player input |
| `try / except ValueError` | Handling non-numeric input |
| Counter variable | Tracking remaining attempts |
| `str.strip().lower()` *(improved version)* | Normalising yes/no and difficulty answers |

---

## Game Rules

1. The computer draws a random integer between **1 and 100** (inclusive).
2. The player has a maximum of **7 valid attempts**.
3. After each wrong guess, the program prints **"Too Low"** or **"Too High"**.
4. An **invalid** input (not a number) or an **out-of-range** input (not in `[1, 100]`) is rejected and **does not consume an attempt**.
5. Finding the number ends the game immediately with a victory message.
6. After 7 unsuccessful attempts, the game is lost and the correct number is revealed.
7. *(Bonus)* Replay mode, difficulty selection

### Function reference

| Function | Responsibility | Returns |
|---|---|---|
| `ask_val()` | Repeatedly prompt until a valid in-range integer is entered | `int` |
| `game()` | Runs one round (secret number, attempts, win/lose), then handles replay | `None` |

### Improved structure (recommended)


---

## Installation & Usage

### Prerequisites

- Python **3.6+** (any standard installation — no external packages required).

### Run the game


# Clone or download the file
git clone <your-repo-url>
cd <repo-folder>

# Launch the game
python pyguess.py

