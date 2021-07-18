from tkinter import *
import utils

root = Tk()
root.geometry('400x400')
root.resizable(0, 0)
root.title('Game-Rock,Paper,Scissors')
root.config(bg='seashell3')

Label(root, text='Rock, Paper ,Scissors', font='arial 20 bold', bg='seashell2').pack()
Label(root, text='choose any one:', font='arial 15 bold', bg='seashell2').place(x=120, y=60)
Label(root, text='1 for rock', font='arial 15 bold', bg='seashell2').place(x=120, y=80)
Label(root, text='2 for paper', font='arial 15 bold', bg='seashell2').place(x=120, y=100)
Label(root, text='3 for scissors', font='arial 15 bold', bg='seashell2').place(x=120, y=120)

output = StringVar()
user_selection = StringVar()

Entry(root, font = 'arial 15', textvariable = user_selection , bg = 'antiquewhite2').place(x=90 , y = 150)
Entry(root, font = 'arial 10 bold', textvariable = output, bg ='antiquewhite2',width = 55,).place(x=20, y = 250)


def play_game():
    try:
        user_pick = utils.get_user_selection(user_selection.get())
        computer_pick = utils.get_computer_selection()

        winner = utils.determine_winner(user_pick, computer_pick)
        print(winner)
        output.set(winner)
    except Exception:
        output.set('Invalid: choose any one -- 1, 2, 3')


def reset_game():
    output.set("")
    user_selection.set("")


def exit_game():
    root.destroy()


Button(root, font = 'arial 13 bold', text = 'PLAY'  ,padx =5,bg ='seashell4' ,command = play_game).place(x=150,y=200)
Button(root, font = 'arial 13 bold', text = 'RESET'  ,padx =5,bg ='seashell4' ,command = reset_game).place(x=70,y=310)
Button(root, font = 'arial 13 bold', text = 'EXIT'  ,padx =5,bg ='seashell4' ,command = exit_game).place(x=230,y=310)


if __name__ == "__main__":
    root.mainloop()
