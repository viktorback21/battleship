from pynput import keyboard

board = []
for i in range(9):
    board.append([0] * 10)


class Ship:
    def __int__(self, cords, destroyed):
        self.cords = cords
        self.destroyed = False



#https://pypi.org/project/pynput/
def on_press(key):
    if key == keyboard.Key.up:
        print("HDSUHUDSIDSiu")
    elif key == keyboard.Key.backspace:
        print("dspÅEAKPÅDSÅJOPhdshoPDS")


def print_board():
    for l in board:
        print(l)


def init_player_board():
    pass


def init_computer_board():
    pass


def make_move():
    pass


def computer_make_move():
    pass


def is_win():
    pass


listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
