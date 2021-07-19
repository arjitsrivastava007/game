# Game - Rock paper Scissors
A python GUI base application which uses Tkinter for interactions.

## Setup Virtual Environment
- Make sure the python version is 3.6
- `https://www.python.org/downloads/`
- `sh setup.sh`

## Start game
- `python3 game.py`
- `1 for player vs computer`
- `2 for computer vs computer`
- `3 for exit app`

After selecting game mode, a window will open where user can play game.
Three buttons will be visible in the window.
1. Play - Starts game
2. Reset - resets game output
3. Exit - closes game window

For Player vs Computer game mode, a user input textbox is provided, through which user can enter 1->rock, 2->paper, 3->scissors, all other invalid inputs.

## What Is Rock Paper Scissors?
We may have played rock paper scissors before. Maybe you’ve used it to decide who pays for dinner or who gets first choice of players for a team.

rock paper scissors is a hand game for two or more players. Participants say “rock, paper, scissors” and then simultaneously form their hands into the shape of a rock (a fist), a piece of paper (palm facing downward), or a pair of scissors (two fingers extended). 
The rules are straightforward:
- `Rock smashes scissors`
- `Paper covers rock`
- `Scissors cut paper`

## Flow Diagram
<p align="center">
  <img src="rock-paper-scissors.jpg"/>
</p>

## Specifications
- `Tkinter is used for GUI based user interaction`

Because string comparisons can cause problems, it’s a good idea to avoid them whenever possible. 
One of the first things your program asks, however, is for the user to input a string! What if the user inputs "Rock" or "rOck" by mistake? 
Capitalization matters, so they won’t be equal:
Henceforth use of Enum is preferred to avoid above problem
```python
class Action(IntEnum):
    rock = 1
    paper = 2
    scissors = 3
```

## Project Extensions
1. Project can be easily extended for lizard and spock, just by updating actions.py file as shown below
```python
class Action(IntEnum):
    rock = 1
    paper = 2
    scissors = 3
    lizard = 3
    spock = 4

    
victories = {
    Action.Scissors: [Action.Lizard, Action.Paper],
    Action.Paper: [Action.Spock, Action.Rock],
    Action.Rock: [Action.Lizard, Action.Scissors],
    Action.Lizard: [Action.Spock, Action.Paper],
    Action.Spock: [Action.Scissors, Action.Rock]
}
```

2. The results of game can be saved in Model(db)

## Running Tests
- `python3 -m unittest`

## Improvements
- `Files computer_vs_computer.py and player_vs_computer.py can be clubbed together`
- `Results of each game can be stored in some db`
- `Performance of game can be improved in GUI based interactions`
- `Adding more test cases`
