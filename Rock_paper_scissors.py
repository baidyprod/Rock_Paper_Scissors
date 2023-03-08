import random
from tkinter import *
from random import choice
from time import time
from os import path
import locale


class Game:
    rules = {
            'Rock': 'Scissors',
            'Scissors': 'Paper',
            'Paper': 'Rock'
            }
    welcome_label = None
    start_game_button = None
    checkbutton_timer = None
    checkbutton_var = None
    log_writer_var = None
    log_writer_checkbutton = None
    mid_game_label = None
    rock_icon = None
    paper_icon = None
    scissors_icon = None
    rock_button = None
    paper_button = None
    scissors_button = None
    player_figure = None
    ai_figure = None
    text_message = None
    winner = None
    late_game_label_1 = None
    late_game_label_2 = None
    late_game_label_3 = None
    play_again_button = None
    timer_start = None
    timer_stop = None
    time = None
    time_label = None
    colors = ('red', 'blue', 'green', 'orange', 'purple')

    def early_game(self):
        self.welcome_label = Label(text='Welcome!', font='Helvetica 24 bold italic', bg='light green', fg='dark green')
        self.start_game_button = Button(text='Start game', fg=random.choice(self.colors),
                                        command=self.early_game_gui_destroy)
        self.checkbutton_var = IntVar()
        self.log_writer_var = IntVar()
        self.checkbutton_timer = Checkbutton(text='Timer', variable=self.checkbutton_var, onvalue=1, offvalue=0)
        self.log_writer_checkbutton = Checkbutton(text='Write logs', variable=self.log_writer_var, onvalue=1,
                                                  offvalue=0)
        self.welcome_label.place(relx=0.5, rely=0.25, anchor=CENTER)
        self.checkbutton_timer.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.log_writer_checkbutton.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.start_game_button.place(relx=0.5, rely=0.6, anchor=CENTER)

    def early_game_gui_destroy(self):
        self.welcome_label.destroy()
        self.checkbutton_timer.destroy()
        self.log_writer_checkbutton.destroy()
        self.start_game_button.destroy()
        self.mid_game()

    def mid_game(self):
        if self.checkbutton_var.get() == 1:
            self.timer_start = time()
        self.mid_game_label = Label(text="What's your figure?")
        self.rock_icon = PhotoImage(file=r'bin/Rock.png').subsample(1, 1)
        self.paper_icon = PhotoImage(file=r'bin/Paper.png').subsample(1, 1)
        self.scissors_icon = PhotoImage(file=r'bin/Scissors.png').subsample(1, 1)
        self.rock_button = Button(text='Rock', fg=random.choice(self.colors), width=70, height=70, image=self.rock_icon,
                                  compound=TOP, command=self.player_figure_rock)
        self.paper_button = Button(text='Paper', fg=random.choice(self.colors), width=70, height=70,
                                   image=self.paper_icon, compound=TOP, command=self.player_figure_paper)
        self.scissors_button = Button(text='Scissors', fg=random.choice(self.colors), width=70, height=70,
                                      image=self.scissors_icon, compound=TOP, command=self.player_figure_scissors)
        self.mid_game_label.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.rock_button.place(relx=0.2, rely=0.5, anchor=CENTER)
        self.paper_button.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.scissors_button.place(relx=0.8, rely=0.5, anchor=CENTER)

    def late_game(self):
        self.ai_figure_define()
        self.define_winner()
        if self.checkbutton_var.get() == 1:
            self.timer_stop = time()
            self.time = round((self.timer_stop - self.timer_start), 2)
        self.mid_game_label.destroy()
        self.rock_button.destroy()
        self.paper_button.destroy()
        self.scissors_button.destroy()
        self.late_game_label_1 = Label(text=f'Your choice is {self.player_figure}', fg=random.choice(self.colors))
        self.late_game_label_2 = Label(text=f'AI choice is {self.ai_figure}', fg=random.choice(self.colors))
        if self.winner == 'Player':
            self.late_game_label_3 = Label(text=self.text_message, fg='dark green', underline=True,
                                           font='Helvetica 14 bold')
        elif self.winner == 'AI':
            self.late_game_label_3 = Label(text=self.text_message, fg='dark red', underline=True,
                                           font='Helvetica 14 bold')
        else:
            self.late_game_label_3 = Label(text=self.text_message, fg='orange', underline=True,
                                           font='Helvetica 14 bold')
        self.play_again_button = Button(text='Play again!', fg=random.choice(self.colors), command=self.restart_game)
        self.late_game_label_1.place(relx=0.5, rely=0.2, anchor=CENTER)
        self.late_game_label_2.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.late_game_label_3.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.play_again_button.place(relx=0.5, rely=0.6, anchor=CENTER)
        if self.checkbutton_var.get() == 1:
            self.time_label = Label(text=f'The game lasted {self.time}s')
            self.time_label.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.checkbutton_timer = Checkbutton(text='Timer', variable=self.checkbutton_var, onvalue=1, offvalue=0)
        self.checkbutton_timer.place(relx=0.5, rely=0.7, anchor=CENTER)
        if self.log_writer_var.get() == 1:
            self.log_writer()

    def player_figure_rock(self):
        self.player_figure = 'Rock'
        self.late_game()

    def player_figure_paper(self):
        self.player_figure = 'Paper'
        self.late_game()

    def player_figure_scissors(self):
        self.player_figure = 'Scissors'
        self.late_game()

    def ai_figure_define(self):
        self.ai_figure = choice(list(self.rules))

    def define_winner(self):
        if (self.player_figure, self.ai_figure) in self.rules.items():
            self.text_message = 'Congrats, You won!'
            self.winner = 'Player'
        elif (self.ai_figure, self.player_figure) in self.rules.items():
            self.text_message = 'Congrats to AI, he won!'
            self.winner = 'AI'
        elif self.player_figure == self.ai_figure:
            self.text_message = 'DRAW!'
            self.winner = 'Draw'
        else:
            self.text_message = 'Something went wrong!'

    def restart_game(self):
        self.late_game_label_1.destroy()
        self.late_game_label_2.destroy()
        self.late_game_label_3.destroy()
        if self.time_label:
            self.time_label.destroy()
        self.checkbutton_timer.destroy()
        self.play_again_button.destroy()
        self.mid_game()

    def log_writer(self):
        if not path.exists("game.res"):
            with open('game.res', 'w') as file:
                file.write('Round\tPlayer\tAI\tResult\tTime\n')
        with open('game.res', 'r') as file:
            game_count = len(file.readlines())
        with open('game.res', 'a') as file:
            if self.time:
                file.write(f'{game_count}\t{self.player_figure}\t{self.ai_figure}\t{self.winner}\t{locale.str(self.time)}\n')
            else:
                file.write(f'{game_count}\t{self.player_figure}\t{self.ai_figure}\t{self.winner}\t''\n')


def main():
    locale.setlocale(locale.LC_ALL, '')
    root = Tk()
    game = Game()
    root.title('Rock-Paper-Scissors')
    root.geometry('400x300')
    root.resizable(width=False, height=False)
    root.eval('tk::PlaceWindow . center')
    game.early_game()
    root.mainloop()


if __name__ == '__main__':
    main()
