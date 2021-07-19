import sys
import os


def game_mode():
    """
    Function to select game mode
    :return: valid integer selection
    """
    try:
        inp = int(input())
    except Exception as err:
        print("Invalid input, enter only integer from above given options")
        inp = game_mode()

    if not inp in [1, 2, 3]:
        print("Invalid input, enter integer from above given options")
        inp = game_mode()

    return inp


def play():
    """
    Function to initialize game
    :return:
    """

    while True:
        print("Select Game mode:")
        print("1 : player vs computer")
        print("2 : computer vs computer")
        print("3 : exit")

        mode = game_mode()
        print(mode)
        if mode == 1:
            os.system("python3 player_vs_computer.py")
        elif mode == 2:
            os.system("python3 computer_vs_computer.py")
        else:
            sys.exit()


if __name__ == "__main__":
    play()
