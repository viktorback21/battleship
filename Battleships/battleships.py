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
    for i in range(10):
        board.append([0] * 10)
    return board


def create_ship(lists, nr):
    if nr < 5:
        listener.join()
        ship = Ship()
        ship.cords = (x, y)
        lists.append(ship)
        nr += 1
        create_ship(lists, nr)
        print(ship.cords)


# https://pypi.org/project/pynput/
def on_press(key):
    global y
    global x
    y1 = y
    x1 = x
    if key == keyboard.Key.up and y1 != 0:
        y1 -= 1
    elif key == keyboard.Key.down and y1 != 9:
        y1 += 1
    elif key == keyboard.Key.left and x1 != 0:
        x1 -= 1
    elif key == keyboard.Key.right and x1 != 9:
        x1 += 1
    elif key == keyboard.Key.enter:
        listener.stop()
    print("\n" * 3)
    print(y1, x1)
    board[y1][x1] = 'x'
    y = y1
    x = x1
    print_board()
    board[y1][x1] = 0


def print_board():
    for l in board:
        print(*l, sep="  ")


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
    listener.start()
    ship_list = []
    create_list()
    create_ship(ship_list, 0)


listener = keyboard.Listener(on_press=on_press)
start()
