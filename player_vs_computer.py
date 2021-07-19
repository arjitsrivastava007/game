from tkinter import *
import utils

root = Tk()
root.geometry("400x400")
root.resizable(0, 0)
root.title("Game-Rock,Paper,Scissors")
root.config(bg="seashell3")

player_selection = StringVar()
computer_selection = StringVar()

Label(root, text="Rock, Paper ,Scissors", font="arial 20 bold", bg="seashell2").pack()

Label(root, text="choose any one:", font="arial 15 bold", bg="seashell2").place(
    x=90, y=60
)
Label(
    root,
    text="1 for rock, 2 for paper, 3 for scissors",
    font="arial 15 bold",
    bg="seashell2",
).place(x=90, y=80)
Label(root, text="2 for paper", font="arial 15 bold", bg="seashell2").place(x=90, y=100)
Label(root, text="3 for scissors", font="arial 15 bold", bg="seashell2").place(
    x=90, y=120
)
Label(root, textvariable=player_selection, font="arial 10 bold", bg="seashell2").place(
    x=90, y=240
)
Label(
    root, textvariable=computer_selection, font="arial 10 bold", bg="seashell2"
).place(x=90, y=260)

output = StringVar()
user_selection = StringVar()
player_selection.set("player selection: ")
computer_selection.set("computer selection: ")

Entry(root, font="arial 15", textvariable=user_selection, bg="antiquewhite2").place(
    x=90, y=160
)
Entry(
    root,
    font="arial 10 bold",
    textvariable=output,
    bg="antiquewhite2",
    width=55,
).place(x=20, y=290)


def play_game():
    """
    Function to play game
    :return:
    """
    try:
        # get selections for player and computer
        user_pick = utils.get_user_selection(user_selection.get())
        computer_pick = utils.get_computer_selection()

        # determine winner
        winner = utils.determine_winner(user_pick, computer_pick, "pvc")

        # display result
        player_selection.set(f"player selection: {user_pick.name}")
        computer_selection.set(f"computer selection: {computer_pick.name}")
        output.set(winner)
    except Exception:
        output.set("Invalid: choose any one -- 1, 2, 3")
        player_selection.set("player selection: ")
        computer_selection.set("computer selection: ")


def reset_game():
    output.set("")
    user_selection.set("")


def exit_game():
    root.destroy()


Button(
    root, font="arial 13 bold", text="PLAY", padx=5, bg="seashell4", command=play_game
).place(x=90, y=200)
Button(
    root, font="arial 13 bold", text="RESET", padx=5, bg="seashell4", command=reset_game
).place(x=70, y=330)
Button(
    root, font="arial 13 bold", text="EXIT", padx=5, bg="seashell4", command=exit_game
).place(x=230, y=330)


if __name__ == "__main__":
    root.mainloop()
