from pynput import keyboard
import os

board = []
x = 0
y = 0


class Ship:
    def __int__(self, cords):
        self.cords = cords
        self.destroyed = False

def create_list():
    for i in range(9):
        board.append([0] * 10)
    return board


def create_ship():
    listener.start()
    listener.join()
    ship = Ship()
    ship.cords = (x, y)
    print(ship.cords)


# https://pypi.org/project/pynput/
def on_press(key):
    global y
    global x
    y1 = y
    x1 = x
    if key == keyboard.Key.up:
        y1 -= 1
    elif key == keyboard.Key.down:
        y1 += 1
    elif key == keyboard.Key.left:
        x1 -= 1
    elif key == keyboard.Key.right:
        x1 += 1
    elif key == keyboard.Key.enter:
        listener.stop()
    print(y1, x1)
    board[y1][x1] = 'x'
    y = y1
    x = x1
    print_board()
    board[y1][x1]=0


def print_board():
    for l in board:
        print(*l, sep = "  ")


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

