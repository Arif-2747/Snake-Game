Python Snake Game
--------------------
This repository contains a classic Snake game implemented in Python. It's a simple, fun, and addictive arcade game where you control a snake, guiding it to eat food and grow longer, all while avoiding collision with its own tail.

Description
---------------------
This project is a recreation of the timeless Snake game. Players control a snake that moves across a grid. The objective is to eat food items that appear randomly on the screen, which makes the snake grow longer. The game ends if the snake hits the boundaries of the game window or collides with its own body. The score increases with each food item consumed.

Features
----------------------
  - Classic Snake game mechanics.
  - Score tracking.
  - Dynamic food generation.
  - Game over detection (wall collision, self-collision).
  - Simple and intuitive keyboard controls.
  - Adjustable game speed (can be modified in code).

Prerequisites
---------------------------
To run this game, you will need:

  - Python 3.13.5
  - turtle module (usually comes pre-installed with Python's standard library)
  - random module (part of Python's standard library, used for food placement)


Installation
------------------------------
1. Install Turtle and Random modules if not installed

        pip install turtle random

2. Run the game: Navigate to the directory where you cloned the repository (or saved the snake_game.py file) and run the script:

       python snake_game.py

How to Play
----------------------------

**Objective - ** The goal is to eat as much food as possible to make your snake long and achieve a high score, without crashing into the walls or your own tail.

**Controls - ** Use the arrow keys on your keyboard to control the snake's direction:

  - Up Arrow: Move the snake upwards.
  - Down Arrow: Move the snake downwards.
  - Left Arrow: Move the snake left.
  - Right Arrow: Move the snake right.

Game Mechanics
-----------------------------
  - **Food: **A red square representing food will appear randomly on the screen. When the snake's head touches the food, the food disappears, the snake grows, and a new food item appears.
  - **Scoring:** Each food item eaten increases your score. The score is displayed at the top of the game window.
  - **Game Over:** The game ends if:
      - The snake's head collides with any part of its own body.
  - **Restart:** To play again after a game over, simply close the game window and re-run the script.

Code Structure
---------------------------------
The game is primarily implemented in a single Python script (snake_game.py). Key components typically include:
  - Game Setup: Initialising the game window, score display, and game elements (snake, food).
  - Snake Movement Logic: Functions to handle the snake's continuous movement and direction changes based on user input.
  - Food Generation: Logic to place food randomly on the screen.
  - Collision Detection: Checks for collisions with walls and the snake's own body.
  - Game Loop: The main loop that updates the game state, redraws elements, and handles events.

Contributing
---------------
You can fix this repository by opening issues and submitting pull requests.

License
---------------
This project is open-source and available under the MIT License.

**Enjoy playing the Snake game!**
