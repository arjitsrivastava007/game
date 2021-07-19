from tkinter import *
import utils

root = Tk()
root.geometry("400x400")
root.resizable(0, 0)
root.title("Game-Rock,Paper,Scissors")
root.config(bg="seashell3")

computer_1_selection = StringVar()
computer_2_selection = StringVar()
output = StringVar()

Label(root, text="Rock, Paper ,Scissors", font="arial 20 bold", bg="seashell2").pack()
Label(
    root, textvariable=computer_1_selection, font="arial 10 bold", bg="seashell2"
).place(x=90, y=150)
Label(
    root, textvariable=computer_2_selection, font="arial 10 bold", bg="seashell2"
).place(x=90, y=180)

computer_1_selection.set("player selection: ")
computer_2_selection.set("computer selection: ")

Entry(
    root,
    font="arial 10 bold",
    textvariable=output,
    bg="antiquewhite2",
    width=55,
).place(x=20, y=250)


def play_game():
    """
    Function to play game
    :return:
    """
    try:
        # get selections for computer
        computer_1_pick = utils.get_computer_selection()
        computer_2_pick = utils.get_computer_selection()
        computer_1_selection.set(f"computer 1 selection: {computer_1_pick.name}")
        computer_2_selection.set(f"computer 2 selection: {computer_2_pick.name}")
        winner = utils.determine_winner(computer_1_pick, computer_2_pick, "cvc")

        # display result

        output.set(winner)
    except Exception:
        output.set("Invalid: choose any one -- 1, 2, 3")
        computer_1_selection.set("player selection: ")
        computer_2_selection.set("computer selection: ")


def reset_game():
    """
    Function to reset output values
    :return:
    """
    output.set("")


def exit_game():
    """
    Function to exit game
    :return:
    """
    root.destroy()


Button(
    root, font="arial 13 bold", text="PLAY", padx=5, bg="seashell4", command=play_game
).place(x=150, y=80)
Button(
    root, font="arial 13 bold", text="RESET", padx=5, bg="seashell4", command=reset_game
).place(x=70, y=310)
Button(
    root, font="arial 13 bold", text="EXIT", padx=5, bg="seashell4", command=exit_game
).place(x=230, y=310)


if __name__ == "__main__":
    root.mainloop()
