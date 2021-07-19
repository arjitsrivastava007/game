import random
from action import Action, victories


def get_user_selection(selection):
    """
    Function to get user selection action object
    :param selection: user selection input
    :return: action object
    """
    try:
        action = Action(int(selection))
        return action
    except Exception as err:
        raise err


def get_computer_selection():
    """
    Function to get computer selection action
    :return: action object
    """
    selection = random.randint(1, len(Action))
    action = Action(selection)
    return action


def get_player_from_mode(mode):
    """
    Function to determine the names of player
    :param mode: 'pvc' -> player vs computer, 'cvc' -> computer vs computer
    :return: first_player, second_palyer string based on mode
    """
    if mode == "pvc":
        first_player = "player"
        second_palyer = "computer"
    else:
        first_player = "computer_1"
        second_palyer = "computer_2"

    return first_player, second_palyer


def determine_winner(user_action, computer_action, mode):
    """
    Function to determine winner for player vs computer game
    :param user_action:
    :param computer_action:
    :param mode: 'pvc' -> player vs computer, 'cvc' -> computer vs computer
    :return: winner
    """
    first_player, second_palyer = get_player_from_mode(mode)
    defeats = victories[user_action]
    if user_action == computer_action:
        return f"Both players selected {user_action.name}. It's a tie!"
    elif computer_action in defeats:
        result = f"{first_player} selection: {user_action.name} beats {second_palyer} selection: {computer_action.name} "
        if mode == "pvc":
            result += "! You win!"
        return result
    else:
        result = f"{second_palyer} selection: {computer_action.name} beats {first_player} selection: {user_action.name} "
        if mode == "pvc":
            result += "! You lose."
        return result
