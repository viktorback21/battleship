from pynput import keyboard

board = []

x = 0
y = 0


def create_list():
    for i in range(9):
        board.append([0] * 10)


class Ship:
    def __int__(self, cords):
        self.cords = cords
        self.destroyed = False


def create_ship():
    listener.start()
    listener.join()
    ship = Ship()
    ship.cords = x
    print(ship.cords)
    print(x)


# https://pypi.org/project/pynput/
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


def start():
    create_list()
    create_ship()


listener = keyboard.Listener(on_press=on_press)
start()
