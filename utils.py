import random
from action import Action


def get_user_selection(selection):
    try:
        action = Action(int(selection))
        return action
    except Exception as err:
        raise err


def get_computer_selection():
    selection = random.randint(1, len(Action))
    action = Action(selection)
    return action


def determine_winner(user_action, computer_action):
    victories = {
        Action.rock: [Action.scissors],  # Rock beats scissors
        Action.paper: [Action.rock],  # Paper beats rock
        Action.scissors: [Action.paper]  # Scissors beats paper
    }

    defeats = victories[user_action]
    if user_action == computer_action:
        return f"Both players selected {user_action.name}. It's a tie!"
    elif computer_action in defeats:
        return f"player selection: {user_action.name} beats computer selection: {computer_action.name}! You win!"
    else:
        return f"computer selection: {computer_action.name} beats player selection: {user_action.name}! You lose."
