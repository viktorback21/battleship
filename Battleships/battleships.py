from pynput import keyboard

player_board = []
computer_board = []
x = 0
y = 0


class Ship:
    def __int__(self, cords):
        self.cords = cords
        self.destroyed = False


def create_list():
    for i in range(10):
        player_board.append([0] * 10)
    return player_board


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


#https://pypi.org/project/pynput/
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
    player_board[y1][x1] = 'x'
    y = y1
    x = x1
    print_board()
    if key == keyboard.Key.enter:
        nr = create_ship(ship_list, nr)
        print(nr)
    else:
        player_board[y1][x1] = 0


def print_board():
    print("        Your board                                                       Enemy board")
    for i in range(10):
        print(*player_board[i], sep="  ", end='                                    ')
        print(*computer_board[i], sep="  ")

def init_player_board():
    pass


def init_computer_board():
    for i in range(10):
        computer_board.append(['*'] * 10)


def make_move(x, y):
    pass


def computer_make_move():
    pass


def is_win():
    pass

def valid_moves(board):
    valid_moves1 = []
    for y, list in enumerate(board):
        for x, spot in enumerate(list):
            if str(spot) == '0':
                valid_moves1.append((x, y))
    return valid_moves1


def start():
    listener.start()
    create_list()
    on_press(keyboard.Key.alt)
    listener.join()


listener = keyboard.Listener(on_press=on_press)


def start():
    create_list()
    init_computer_board()
    listener.start()
    listener.join()


start()
