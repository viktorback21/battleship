from pynput import keyboard

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


def create_ship(lists, number):
    if number < 5:
        ship = Ship()
        ship.cords = (x, y)
        lists.append(ship)
        number += 1
        if number == 5:
            for s in ship_list:
                print(s.cords)
            listener.stop()
        return number


ship_list = []

nr = 0


# https://pypi.org/project/pynput/
def on_press(key):
    global nr
    global ship_list
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
    print("\n" * 3)
    print(y1, x1)
    board[y1][x1] = 'x'
    y = y1
    x = x1
    print_board()
    if key == keyboard.Key.enter:
        nr = create_ship(ship_list, nr)
        print(nr)
    else:
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


listener = keyboard.Listener(on_press=on_press)


def start():
    create_list()
    listener.start()
    listener.join()


start()
